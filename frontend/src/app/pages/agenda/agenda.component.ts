import { Component , OnInit ,  Input, Output, EventEmitter } from '@angular/core';
import timeGridPlugin from '@fullcalendar/timegrid';
import ptBrLocale from '@fullcalendar/core/locales/pt-br';
import interactionPlugin, { Draggable } from '@fullcalendar/interaction';
import listGridPlugin from '@fullcalendar/list';
import dayGridPlugin from '@fullcalendar/daygrid';
import multiMonthPlugin from '@fullcalendar/multimonth'


@Component({
  selector: 'app-agenda',
  templateUrl: './agenda.component.html',
  styleUrls: ['./agenda.component.scss']
})
export class AgendaComponent implements OnInit{

  
  public minHour = 8;

  public maxHour = 19;

  public visible = false



  currentEvents:any = []
  countries: any[] | undefined;
  selectedCountry: any ;

  ngOnInit() {  }

  calendarOptions = {
    plugins: [timeGridPlugin, interactionPlugin, listGridPlugin, dayGridPlugin, multiMonthPlugin ],
    initialView: 'timeGridWeek',
    themeSystem: 'standart',
    headerToolbar: {
      left: 'dayGridMonth,timeGridDay,timeGridWeek,listWeek,multiMonthYear,profissionais',
      center: 'title',
      right: 'prev,today,dataPicker,next'
    },
    weekends: false,
    events: [
      { title: 'Evento 2', start: '2023-10-27T14:00:00', end: '2023-10-27T16:00:00' },
      { title: 'Evento 3', start: '2023-10-27T14:00:00', end: '2023-10-27T16:04:00' }

    ],
    locale: ptBrLocale,
    slotMinTime: `${this.minHour}:00`,
    slotMaxTime: `${this.maxHour}:00`,
    droppable: true,
    eventColor: '#3c8dbc',
    eventBorderColor: '#fff',
    eventTextColor: '#fff',
    editable: true,
    selectable: true,
    select: this.handleDateSelect.bind(this),
    eventClick: this.handleEventClick.bind(this),
    allDayText: '',
    allDaySlot: false,
    customButtons: {
      profissionais: {
        text: 'Profissionais',
        click: function() {
          console.log('clicked the custom button!');
        }
      },
      dataPicker: {
        text: 'Selecionar data',
        click: function() {
          console.log('clicked the custom button!');
        }
      },
    },
    buttonText: {
      today:    'Hoje',
      month:    'Mês',
      week:     'Semana',
      day:      'Dia',
      list:     'Lista do dia'
    },
    height: 680,

  };


  handleDateSelect(selectInfo: any) {
    // const title = prompt('Please enter a new title for your event');
    const calendarApi = selectInfo.view.calendar;
    calendarApi.unselect(); 
    this.visible = true
    // if (title) {
    //   calendarApi.addEvent({
    //     title,
    //     start: selectInfo.startStr,
    //     end: selectInfo.endStr,
    //     allDay: selectInfo.allDay
    //   });
    // }
  }

  handleEventClick(clickInfo: any) {
    if (confirm(`Are you sure you want to delete the event '${clickInfo.event.title}'`)) {
      clickInfo.event.remove();
    }
  }



  
  



  
}
