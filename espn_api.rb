

class Espn_api
  def initialize
    @url_prefix = "https://www.espn.com/nfl/boxscore/_/gameId/"
  end
  def get_team_stats(game_id)
    team_stats_endpoint = URI(@url_prefix + game_id.to_s)
    team_stats_response = Net::HTTP.get_response(team_stats_endpoint)
    parsed_stats = Nokogiri::HTML.parse(team_stats_response)

end

espn = Espn_api.new(401326600)
puts espn.get_team_stats
