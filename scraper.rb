require 'uri'
require 'net/http'
require 'json'
require_relative 'game'
require_relative 'team'

game_endpoint = URI('http://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard')
game_response = Net::HTTP.get_response(game_endpoint)
game_object = JSON.parse(game_response.body)

games = []
live_games = []

for game in game_object['events'] do

  game_id = game['id']
  game_name = game['name']
  game_date = game['date']

  for team in game['competitions']['competitors'] do
    if team['homeAway'] == 'home'
      home_team_name = team['team']['displayName']
      home_team_id = team['team']['id']
    else
      away_team_name = team['team']['displayName']
      away_team_id = team['team']['id']
    end
  end

  home_roster_endpoint = URI("https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/events/#{game_id}/competitions/#{game_id}/competitors/#{home_team_id}/roster)"
  away_roster_endpoint = URI("https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/events/#{game_id}/competitions/#{game_id}/competitors/#{away_team_id}/roster)"

  home_roster_response = Net::HTTP.get_response(home_roster_endpoint)
  away_roster_response = Net::HTTP.get_response(away_roster_endpoint)

  home_roster_object = JSON.parse(home_roster_response.body)
  away_roster_object = JSON.parse(away_roster_response.body)

  games << Game.new(game_id, game_name, game_date, home_team, away_team)
end

for game in games do
  if game.is_live?
    puts game.name
    puts game.id
  end
end
