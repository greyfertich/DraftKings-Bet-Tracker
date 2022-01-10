require 'uri'
require 'net/http'
require 'json'
require 'nokogiri'
require_relative 'game'
require_relative 'team'
require_relative 'player'
require_relative 'roster'

game_endpoint = URI('http://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard')
game_response = Net::HTTP.get_response(game_endpoint)
game_object = JSON.parse(game_response.body)

games = []
live_games = []

for game_data in game_object['events'] do
  game_id = game_data['id']
  game_name = game_data['name']
  game_date = game_data['date']

  game = Game.new(game_id, game_name, game_date)

  if game.is_live?
    for team in game_data['competitions'][0]['competitors'] do
      if team['homeAway'] == 'home'
        home_team_name = team['team']['displayName']
        home_team_id = team['team']['id']
      else
        away_team_name = team['team']['displayName']
        away_team_id = team['team']['id']
      end
    end

    home_roster_endpoint = URI("https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/events/#{game_id}/competitions/#{game_id}/competitors/#{home_team_id}/roster")
    away_roster_endpoint = URI("https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/events/#{game_id}/competitions/#{game_id}/competitors/#{away_team_id}/roster")

    home_roster_response = Net::HTTP.get_response(home_roster_endpoint)
    away_roster_response = Net::HTTP.get_response(away_roster_endpoint)

    home_roster_object = JSON.parse(home_roster_response.body)
    away_roster_object = JSON.parse(away_roster_response.body)

    home_players = []
    away_players = []

    for player_object in home_roster_object["entries"] do
      id = player_object['playerId']
      name = player_object["displayName"]
      number = player_object["jersey"]
      home_players << Player.new(id, name, number)
    end
    for player_object in away_roster_object["entries"] do
      id = player_object['playerId']
      name = player_object["displayName"]
      number = player_object["jersey"]
      away_players << Player.new(id, name, number)
    end

    home_roster = Roster.new(home_team_name, home_players)
    away_roster = Roster.new(away_team_name, away_players)

    home_team = Team.new(home_team_id, home_team_name, home_roster)
    away_team = Team.new(away_team_id, away_team_name, away_roster)

    game.home_team = home_team
    game.away_team = away_team

    games << game
  end
end

for game in games do
  if game.is_live?
    puts game.name
    puts game.id
    # game.get_rosters
  end
end
