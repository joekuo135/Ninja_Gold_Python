# Ninja_Gold_Python
Create a simple game to test understanding of flask, implement the functionality below<br>
and helps a ninja make some money!
<ul>
<li>When you start the game, your ninja should have 0 gold.</li>
<li>The ninja can go to different places (farm, cave, house, casino) and earn different amounts of gold.</li>
<li>In the case of a casino, your ninja can earn or LOSE up to 50 golds.</li>
<li>Create a web app that allows this ninja to earn gold and to display past activities of this ninja.</li>
</ul>
Guidelines:(Refer to the wireframe below)<br>
<ul>
  <li>Have the four forms appear when the user goes to http://localhost:5000.</li>
  <li>For the farm, your form would look something like:<br>
    form action="/process_money" method="post"
    input type="hidden" name="building" value="farm
    input type="submit" value="Find Gold!"</li>

  <li>Include a hidden value in the form and have each form submit the form information to /process_money.</li>
  <li>Have /process_money determine how much gold the user should have.</li>
  <li>You should only have 2 routes -- '/' and '/process_money' (reset can be another route if you implement this feature).</li>
</ul>


Please make sure that...
<ul>
  <li>We don't want to have to go to "/gold/index" or other URL to see this app</li>
  <li>The forms are sent to "/process_money" and not any other URL.</li>
  <li>The activities are stored in the session. No need to store anything in the database.</li> 
</ul>
