-- Convert simple, flat unordered lists into compact paragraphs.
-- Complex/nested lists retain their structure and can be styled separately.
function BulletList(el)
  local result = {}
  for _, item in ipairs(el.content) do
    if #item ~= 1 or (item[1].t ~= "Plain" and item[1].t ~= "Para") then
      return nil
    end
    table.insert(result, pandoc.Para(item[1].content))
  end
  return pandoc.Div(result, pandoc.Attr("", {"compact-items"}))
end
