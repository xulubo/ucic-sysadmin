function read_query(packet)
 if packet:byte() == proxy.COM_QUERY 
 then
 local query = packet:sub(2)
 print("SQL>" .. query )
 end
end
