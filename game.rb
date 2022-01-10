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
    chargers_game_time = DateTime.strptime("2022-01-09T20:50Z", '%Y-%m-%dT%H:%M%Z').to_time
    # return (current_time >= @date and ((current_time - @date) / 3600) <= 5)
    return (chargers_game_time >= @date and ((chargers_game_time - @date) / 3600) <= 5)
  end
end


# DateTime.strptime('2001-02-03T04:05:06+07:00', '%Y-%m-%dT%H:%M%Z')
                          #=> #<DateTime: 2001-02-03T04:05:06+07:00 ...>
