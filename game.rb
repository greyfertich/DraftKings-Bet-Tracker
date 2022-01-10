require 'date'
require_relative 'team'

class Game
  attr_accessor :home_team, :away_team
  attr_reader :id, :name, :date, :home_team, :away_team
  def initialize(id, name, date)
    @id = id
    @name = name
    @date = DateTime.strptime(date, '%Y-%m-%dT%H:%M%Z').to_time
  end
  def is_live?
    current_time = DateTime.now.to_time
    chargers_game_time = DateTime.strptime("2022-01-10T01:50Z", '%Y-%m-%dT%H:%M%Z').to_time
    # return (current_time >= @date and ((current_time - @date) / 3600) <= 5)
    return (chargers_game_time >= @date and ((chargers_game_time - @date) / 3600) <= 1)
  end
  def get_rosters
    if !home_team and !away_team
      puts "No rosters to show for #{@name}"
      return
    end
    if home_team
      puts "Home: #{home_team.name}"
      home_team.roster.players.each_with_index do |player, index|
        puts "#{index+1}: #{player.name}, \##{player.number}, id: #{player.id}"
      end
    end
    if away_team
      puts "Away: #{away_team.name}"
      away_team.roster.players.each_with_index do |player, index|
        puts "#{index+1}: #{player.name}, \##{player.number}, id: #{player.id}"
      end
    end
  end
end


# DateTime.strptime('2001-02-03T04:05:06+07:00', '%Y-%m-%dT%H:%M%Z')
                          #=> #<DateTime: 2001-02-03T04:05:06+07:00 ...>
