require 'uri'
require 'net/http'
require 'nokogiri'

class Espn_api
  def initialize
    @url_prefix = "https://www.espn.com/nfl/boxscore/_/gameId/"
  end
  def get_team_stats(game_id)
    team_stats_endpoint = URI(@url_prefix + game_id.to_s)
    team_stats_response = Net::HTTP.get_response(team_stats_endpoint)
    parsed_stats = Nokogiri::HTML(team_stats_response.body)
    # parsed_stats = Nokogiri::Slop(team_stats_response.body)
    class_name = "mod-data"
    @stats = parsed_stats.xpath("//*[@class=\"#{class_name}\"]")
    count = 0
    puts @stats.search("td")
    for table in @stats.search("td") do
      count += 1
      puts table
      puts "\n\n"
    end
    # puts "count " + count.to_s
    # @stats = @stats.xpath("//td").first

    # @stats = parsed_stats.xpath("//*[@class=\"#{class_name}\"]")
  end
end

espn = Espn_api.new
espn.get_team_stats(401326600)
