# Obsolete !!! Replace by another project [spm](https://github.com/abiaog/spm)

# TextPM
A project management tool based on plain text.

## Ideas
I used to manage project by Excel by which I can run Agile and Scrum.
Sometimes, I need to draw Gantt chart for demonstrating the progress of the project.
I was thinking about how to combine the two things together?
On one hand, Agile is flexible and embrace of change. On the other hand, Gantt chart looks well planned.
Also, I was thinking another problem, how to manage project based on plain text?
Since I am a fan of VIM, and I really like the plain text based environment.
Actually, plain text is indeed efficient than GUI.
I studied several tools, for example, TaskJuggler, OrgMode, PlantUML Gannt and Python Task Planner.
Each of them has its own pros and cons, but I learnt a lot from them.
So I decided to do an efficient, simple, good enough project management tool for myself.
Of course, it's based on plain text!!!

### Use Excel as whiteboard
### Convert Excel to plain text `csv`


## Format

```
Priority,  	Task,  			Task-Id,  Owner,  Status,   	Effort     , Dependencies
1       ,   task1 ,		        id1   ,	  a   ,  Ongoing,		5  ,   
2       , > subtask11 ,			id11  ,	  a   ,  Ongoing,		5  ,  
3       , >> sub subtask111 ,	        id111 ,	  a   ,  Ongoing,		5  ,  id2
1       ,   task2 ,		        id2   ,	  a   ,  Ongoing,		5  ,   

>  : used for identifying sub task.
>> : used for identifying sub sub task.
>>>: Have a guess :)
```

## Chart

Gantt Chart 	: based on PlantUML Gannt

Burnndown Chart : inside Excel



