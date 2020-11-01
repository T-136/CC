require "turtle"

local function refuel()
    for i=1,16 do
        local data = turtle.getItemDetail(i)
        if data and string.match(data['name'], "coal") then
            turtle.select(i)
            turtle.refuel(15)
            return true
        end
    end
    return false
end

local function plantSeed()
    turtle.select(1)
    turtle.placeDown()
end

local function checkAndGo()
    local success, data = turtle.inspectDown()
    print(success, data)
    success, data = turtle.inspectDown()
    if success then
        if data["state"]["age"] == 7 then
            turtle.digDown("right")
            plantSeed()
        end
    else
        turtle.digDown("right")
        plantSeed()
    end
    turtle.forward()
end



local function run(size)
    turtle.forward()

    for x=1,size do
        for y=1,size-1 do
            checkAndGo()
        end
        if x < size then
            if (x % 2 == 1) then
                turtle.turnRight()
                checkAndGo()
                turtle.turnRight()
            else
                turtle.turnLeft()
                checkAndGo()
                turtle.turnLeft()
            end
        end
    end
    turtle.turnRight()

    for y=1, size-1 do
        turtle.forward()
    end

    turtle.turnRight()
    turtle.back()
end

print("FIELD SIZE: ")
local size = tonumber(read())

while true do
    refuel()
    run(size)
    os.sleep(60)
end
