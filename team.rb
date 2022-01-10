

class Team
  attr_reader :name, :roster
  def initialize(id, name, roster)
    @id = id
    @name = name
    @roster = roster
  end
end
