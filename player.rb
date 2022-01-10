

class Player
  attr_reader :id, :name, :number
  def initialize(id, name, number)
    @id = id
    @name = name
    @number = number
  end
end
