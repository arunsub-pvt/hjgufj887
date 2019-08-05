import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "harshithaphaniwedding@gmail.com"
password = "Arunkiran1@"


def sendmail(recepient, receiver_email):

    # Create the plain-text and HTML version of your message
    html = """\
<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office" style="background:#f1f1f1;margin:0 auto ;padding:0 ;height:100% ;width:100% ;">
  <head></head>
    <meta charset="utf-8">
    <!-- utf-8 works for most cases -->
    <meta name="viewport" content="width=device-width">
    <!-- Forcing initial-scale shouldn't be necessary -->
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <!-- Use the latest (edge) version of IE rendering engine -->
    <meta name="x-apple-disable-message-reformatting">
    <!-- Disable auto-scale in iOS 10 Mail entirely -->
    <title></title>
    <!-- The title tag shows in email notifications, like Android 4.4. -->
    <link href="https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700" rel="stylesheet">
    <!-- CSS Reset : BEGIN -->
  <body width="100%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;background:#f1f1f1;font-family:'Poppins', sans-serif;font-weight:400;font-size:15px;line-height:1.8;color:rgba(0, 0, 0, .4);margin:0 auto ;padding:0 ;height:100% ;width:100% ;margin: 0; padding: 0 ; mso-line-height-rule: exactly; background-color: #222222;">
    <style>
      .heading-section .subheading::after{position:absolute;left:0;right:0;bottom:-10px;content:'';width:100%;height:2px;background:#0d0cb5;margin:0 auto}
    </style>
    <style type="text/css">
      /* What it does: Stops email clients resizing small text. */
              /* What it does: Centers email on Android 4.4 */
              /* What it does: Stops Outlook from adding extra spacing to tables. */
              /* What it does: A work-around for email clients meddling in triggered links. */
              *[x-apple-data-detectors],
              /* iOS */
              .unstyle-auto-detected-links *,
              .aBn {
                  border-bottom: 0 ;
                  cursor: default ;
                  color: inherit ;
                  text-decoration: none ;
                  font-size: inherit ;
                  font-family: inherit ;
                  font-weight: inherit ;
                  line-height: inherit ;
              }
              /* What it does: Prevents Gmail from displaying a download button on large, non-linked images. */
              /* If the above doesn't work, add a .g-img class to any image in question. */
              /* What it does: Removes right gutter in Gmail iOS app: https://github.com/TedGoas/Cerberus/issues/89  */
              /* Create one of these media queries for each additional viewport size you'd like to fix */
              /* iPhone 4, 4S, 5, 5S, 5C, and 5SE */
              @media only screen and (min-device-width: 320px) and (max-device-width: 374px) {
                  u ~ div .email-container {
                      min-width: 320px ;
                  }
              }
              /* iPhone 6, 6S, 7, 8, and X */
              @media only screen and (min-device-width: 375px) and (max-device-width: 413px) {
                  u ~ div .email-container {
                      min-width: 375px ;
                  }
              }
              /* iPhone 6+, 7+, and 8+ */
              @media only screen and (min-device-width: 414px) {
                  u ~ div .email-container {
                      min-width: 414px ;
                  }
              }
              /*LOGO*/
              /*HEADING SECTION*/
              /*BLOG*/
              /*TESTIMONY*/
              @media screen and (max-width: 500px) {
                  .icon {
                      text-align: left;
                  }
                  .text-services {
                      padding-left: 0;
                      padding-right: 20px;
                      text-align: left;
                  }
              }
    </style>
    <!-- CSS Reset : END -->
    <!-- Progressive Enhancements : BEGIN -->
    <center style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;width: 100%; background-color: #f1f1f1;">
      <div style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;display: none; font-size: 1px;max-height: 0px; max-width: 0px; opacity: 0; overflow: hidden; mso-hide: all; font-family: sans-serif;">
        &zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;
        </div>
      <div style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;max-width: 600px; margin: 0 auto;" class="email-container">
        <!-- BEGIN BODY -->
        <table align="center" role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;border-spacing:0 ;border-collapse:collapse ;table-layout:fixed ;margin:0 auto ;margin: auto;">
          <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
            <td valign="top" class="bg_white" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;background:#ffffff;mso-table-lspace:0pt ;mso-table-rspace:0pt ;padding: 1em 2.5em; text-align: center;">
              <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;border-spacing:0 ;border-collapse:collapse ;table-layout:fixed ;margin:0 auto ;">
                <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">Rotate your phone to landscape to view this mail better!</tr>
              </table>
            </td>
          </tr>
          <!-- end tr -->
          <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
            <td valign="middle" class="hero bg_white" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;background:#ffffff;position:relative;z-index:0;mso-table-lspace:0pt ;mso-table-rspace:0pt ;background-image: url(https://raw.githubusercontent.com/arunsub-pvt/hjgufj887/master/images/bg_1.jpg); background-size: cover; height: 400px;">
              <div class="overlay" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;position:absolute;top:0;left:0;right:0;bottom:0;content:'';width:100%;background:#000000;z-index:-1;opacity:.3;"></div>
              <table style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;border-spacing:0 ;border-collapse:collapse ;table-layout:fixed ;margin:0 auto ;">
                <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                  <td style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;">
                    <div class="text" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;color:rgba(255, 255, 255, .8);padding: 0 3em; text-align: justify;">
                      <h2 style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;font-family:'Poppins', sans-serif;color:#000000;margin-top:0;color:#ffffff;font-size:30px;margin-bottom:0;">Hi _$$$_!</h2>
                      <p style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">Thank you for responding to our invite. We're so happy that you could be there for our special moment. As we get busy getting ready for the big day, we're leaving you in the safe hands of our master of ceremonies - Arun for all practical purposes and logistics. Hope you have as much fun as we do and see you at the wedding!</p>
                    </div>
                    <div class="text" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;color:rgba(255, 255, 255, .8);padding: 0 3em; text-align: right;">
                      Love,
                                        <br style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                       Harshitha & Phani
                                    </div>
                  </td>
                </tr>
              </table>
            </td>
          </tr>
          <!-- end tr -->
          <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
            <td class="bg_white" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;background:#ffffff;mso-table-lspace:0pt ;mso-table-rspace:0pt ;">
              <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;border-spacing:0 ;border-collapse:collapse ;table-layout:fixed ;margin:0 auto ;">
                <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                  <td style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;">
                    <table style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;border-spacing:0 ;border-collapse:collapse ;table-layout:fixed ;margin:0 auto ;">
                      <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                        <div class="heading-section" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;text-align: center; padding-top: 20px;">
                          <h2 style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;font-family:'Poppins', sans-serif;color:#000000;font-size:20px;margin-top:0;line-height:1.4;font-weight:700;text-transform:uppercase;margin-block-end: 0;">The Master of Ceremonies</h2>
                        </div>
                      </tr>
                      <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                        <td style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;width=80%;">
                          <div style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;text-align: justify; padding: 0 20px 0 40px; display: block;">
                            <p style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">Hello all, let me introduce myself! I am <b style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">Arun</b> and to those who don't know what I do at the wedding from the title, I'm the conductor that orchestrates the entire wedding ensemble before and on the day of the wedding. For you - the guests, I'll be your point of contact from here on so you don't have to disturb the bride and the groom as they approach their special day.
                                                        <br style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                               Let's start with the events of the day...
                                                    </p>
                          </div>
                        </td>
                        <td style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;width=20%;">
                          <img src="https://raw.githubusercontent.com/arunsub-pvt/hjgufj887/master/images/hi.png" alt="" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;-ms-interpolation-mode:bicubic;text-align: left; height: 250px; max-height: 250px; width: auto; padding-right: 40px;">
                        </td>
                      </tr>
                    </table>
                    <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;border-spacing:0 ;border-collapse:collapse ;table-layout:fixed ;margin:0 auto ;">
                      <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                        <td valign="top" width="20%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;background:rgba(0, 0, 0, .03);mso-table-lspace:0pt ;mso-table-rspace:0pt ;padding-top: 20px;" class="services">
                          <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;border-spacing:0 ;border-collapse:collapse ;table-layout:fixed ;margin:0 auto ;">
                            <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                              <td class="text-services" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;padding:10px 10px 0;text-align:center;mso-table-lspace:0pt ;mso-table-rspace:0pt ;">
                                <h3 style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;font-family:'Poppins', sans-serif;color:#000000;margin-top:0;font-size:16px;font-weight:600;">15:15</h3>
                                <p style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">Doors Open</p>
                              </td>
                            </tr>
                          </table>
                        </td>
                        <td valign="top" width="20%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;background:rgba(0, 0, 0, .03);mso-table-lspace:0pt ;mso-table-rspace:0pt ;padding-top: 20px; background: rgba(0,0,0,.08);" class="services">
                          <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;border-spacing:0 ;border-collapse:collapse ;table-layout:fixed ;margin:0 auto ;">
                            <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                              <td class="text-services" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;padding:10px 10px 0;text-align:center;mso-table-lspace:0pt ;mso-table-rspace:0pt ;">
                                <h3 style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;font-family:'Poppins', sans-serif;color:#000000;margin-top:0;font-size:16px;font-weight:600;">16:15</h3>
                                <p style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">Ceremony</p>
                              </td>
                            </tr>
                          </table>
                        </td>
                        <td valign="top" width="20%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;background:rgba(0, 0, 0, .03);mso-table-lspace:0pt ;mso-table-rspace:0pt ;padding-top: 20px;" class="services">
                          <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;border-spacing:0 ;border-collapse:collapse ;table-layout:fixed ;margin:0 auto ;">
                            <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                              <td class="text-services" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;padding:10px 10px 0;text-align:center;mso-table-lspace:0pt ;mso-table-rspace:0pt ;">
                                <h3 style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;font-family:'Poppins', sans-serif;color:#000000;margin-top:0;font-size:16px;font-weight:600;">17:00</h3>
                                <p style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">Reception</p>
                              </td>
                            </tr>
                          </table>
                        </td>
                        <td valign="top" width="20%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;background:rgba(0, 0, 0, .03);mso-table-lspace:0pt ;mso-table-rspace:0pt ;padding-top: 20px; background: rgba(0,0,0,.08);" class="services">
                          <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;border-spacing:0 ;border-collapse:collapse ;table-layout:fixed ;margin:0 auto ;">
                            <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                              <td class="text-services" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;padding:10px 10px 0;text-align:center;mso-table-lspace:0pt ;mso-table-rspace:0pt ;">
                                <h3 style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;font-family:'Poppins', sans-serif;color:#000000;margin-top:0;font-size:16px;font-weight:600;">19:00</h3>
                                <p style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">Dinner</p>
                              </td>
                            </tr>
                          </table>
                        </td>
                        <td valign="top" width="20%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;background:rgba(0, 0, 0, .03);mso-table-lspace:0pt ;mso-table-rspace:0pt ;padding-top: 20px;" class="services">
                          <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;border-spacing:0 ;border-collapse:collapse ;table-layout:fixed ;margin:0 auto ;">
                            <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                              <td class="text-services" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;padding:10px 10px 0;text-align:center;mso-table-lspace:0pt ;mso-table-rspace:0pt ;">
                                <h3 style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;font-family:'Poppins', sans-serif;color:#000000;margin-top:0;font-size:16px;font-weight:600;">21:00</h3>
                                <p style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">Party</p>
                              </td>
                            </tr>
                          </table>
                        </td>
                      </tr>
                    </table>
                    <div style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;text-align: justify; padding: 20px 40px 0 40px; padding-bottom: 40px; display: block;">
                      The times have slightly changed from the invites because of all the subsequent planning. Nevertheless, the message is, <b style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">PLEASE BE ON TIME!!</b>
                    </div>
                  </td>
                </tr>
                <!-- end: tr -->
                <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                  <td valign="middle" class="counter" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;width:100%;position:relative;z-index:0;mso-table-lspace:0pt ;mso-table-rspace:0pt ;background-image: url(https://raw.githubusercontent.com/arunsub-pvt/hjgufj887/master/images/bg_2.jpg); background-size: cover; padding: 4em 0;">
                    <div class="overlay" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;position:absolute;top:0;left:0;right:0;bottom:0;content:'';width:100%;background:#000000;z-index:-1;opacity:.3;"></div>
                    <table style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;border-spacing:0 ;border-collapse:collapse ;table-layout:fixed ;margin:0 auto ;">
                      <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                        <td valign="middle" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;">
                          <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;border-spacing:0 ;border-collapse:collapse ;table-layout:fixed ;margin:0 auto ;">
                            <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                              <div class="heading-section-white" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;color:rgba(255, 255, 255, .8);text-align: center; padding-top: 20px;">
                                <h2 style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;font-family:'Poppins', sans-serif;color:#000000;margin-top:0;font-family:line-height: 1;padding-bottom:0;color:#ffffff;margin-block-end: 0;">HOW TO GET THERE?</h2>
                              </div>
                            </tr>
                          </table>
                        </td>
                      </tr>
                    </table>
                  </td>
                </tr>
                <!-- end: tr -->
                <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                  <td class="bg_white email-section" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;background:#ffffff;padding:2.5em;mso-table-lspace:0pt ;mso-table-rspace:0pt ;">
                    <table style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;border-spacing:0 ;border-collapse:collapse ;table-layout:fixed ;margin:0 auto ;">
                      <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                        <td style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;">
                          <div class="heading-section" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;text-align: justify; padding: 0 20px;">
                            <p style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">All of the day's events take place at the <a href="https://goo.gl/maps/9goh1ZQECykYgjQw6" target="_blank">Duivenvoorde Castle</a> in Voorschoten. Here's a detailed map of the surroundings:</p>
                          </div>
                        </td>
                      </tr>
                    </table>
                    <table style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;border-spacing:0 ;border-collapse:collapse ;table-layout:fixed ;margin:0 auto ;">
                      <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                        <img src="https://raw.githubusercontent.com/arunsub-pvt/hjgufj887/master/images/way.jpg" alt="" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;-ms-interpolation-mode:bicubic;width: 100%; max-width: 600px; height: auto; margin: auto; display: block;">
                      </tr>
                    </table>
                    <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;border-spacing:0 ;border-collapse:collapse ;table-layout:fixed ;margin:0 auto ;">
                      <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                        <td valign="middle" width="40%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;">
                          <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;border-spacing:0 ;border-collapse:collapse ;table-layout:fixed ;margin:0 auto ;">
                            <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                              <td style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;padding-top: 20px; padding-left: 20px;">
                                <img src="https://raw.githubusercontent.com/arunsub-pvt/hjgufj887/master/images/car.png" alt="" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;-ms-interpolation-mode:bicubic;width: 100%; max-width: 600px; height: auto; margin: auto; display: block;">
                              </td>
                            </tr>
                          </table>
                        </td>
                        <td valign="middle" width="60%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;">
                          <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;border-spacing:0 ;border-collapse:collapse ;table-layout:fixed ;margin:0 auto ;">
                            <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                              <td style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;padding-top: 20px;">
                                <div class="heading-section" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;text-align: justify; padding: 0 20px;">
                                  <p style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">The best way to get to the location is by car. There is plenty of parking inside the estate. So if you don't have a car, find a buddy to carpool with!</p>
                                </div>
                              </td>
                            </tr>
                          </table>
                        </td>
                      </tr>
                    </table>
                    <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;border-spacing:0 ;border-collapse:collapse ;table-layout:fixed ;margin:0 auto ;">
                      <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                        <td valign="middle" width="70%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;">
                          <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;border-spacing:0 ;border-collapse:collapse ;table-layout:fixed ;margin:0 auto ;">
                            <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                              <td style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;padding-top: 20px;">
                                <div class="heading-section" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;text-align: justify; padding: 0 20px;">
                                  <p style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">You could also come by public transport. Your best bet then is to get to Den Haag Centraal and then take bus 45 or 46 or get to Leiden Centraal and take bus 45. Either way, the bus stop nearest to the castle is <b style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">Kniplaan</b>. From the bus stop, it's roughly a 12 minute walk to the castle.</p>
                                </div>
                              </td>
                            </tr>
                          </table>
                        </td>
                        <td valign="middle" width="30%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;">
                          <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;border-spacing:0 ;border-collapse:collapse ;table-layout:fixed ;margin:0 auto ;">
                            <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                              <td style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;padding-top: 20px; padding-right: 20px;">
                                <img src="https://raw.githubusercontent.com/arunsub-pvt/hjgufj887/master/images/train.png" alt="" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;-ms-interpolation-mode:bicubic;width: 100%; max-width: 600px; height: auto; margin: auto; display: block;">
                              </td>
                            </tr>
                          </table>
                        </td>
                      </tr>
                      <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                        <table style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;border-spacing:0 ;border-collapse:collapse ;table-layout:fixed ;margin:auto ;">
                          <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                            <td style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;">
                              <div class="heading-section" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;text-align: justify; padding: 0 20px;">
                                <p style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;color: #ff0000;"> <b style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">WATCH OUT!</b> Stupid NS is carrying out works on the tracks in that weekend and there will be limited or no trains between Den Haag Centraal and Rotterdam Centraal. There will be buses instead though. Please take this longer time into account while planning your trip!</p>
                              </div>
                            </td>
                          </tr>
                        </table>
                      </tr>
                    </table>
                  </td>
                </tr>
                <!-- end: tr -->
                <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                  <td valign="middle" class="counter" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;width:100%;position:relative;z-index:0;mso-table-lspace:0pt ;mso-table-rspace:0pt ;background-image: url(https://raw.githubusercontent.com/arunsub-pvt/hjgufj887/master/images/guests.jpg); background-size: cover; padding: 4em 0;">
                    <div class="overlay" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;position:absolute;top:0;left:0;right:0;bottom:0;content:'';width:100%;background:#000000;z-index:-1;opacity:.3;"></div>
                    <table style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;border-spacing:0 ;border-collapse:collapse ;table-layout:fixed ;margin:0 auto ;">
                      <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                        <td valign="middle" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;">
                          <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;border-spacing:0 ;border-collapse:collapse ;table-layout:fixed ;margin:0 auto ;">
                            <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                              <div class="heading-section-white" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;color:rgba(255, 255, 255, .8);text-align: center; padding-top: 20px;">
                                <h2 style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;font-family:'Poppins', sans-serif;color:#000000;margin-top:0;font-family:line-height: 1;padding-bottom:0;color:#ffffff;margin-block-end: 0;">WHAT TO WEAR?</h2>
                              </div>
                            </tr>
                          </table>
                        </td>
                      </tr>
                    </table>
                  </td>
                </tr>
                <!-- end tr -->
                <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                  <td class="bg_white email-section" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;background:#ffffff;padding:2.5em;mso-table-lspace:0pt ;mso-table-rspace:0pt ;">
                    <table style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;border-spacing:0 ;border-collapse:collapse ;table-layout:fixed ;margin:0 auto ;">
                      <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                        <td style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;">
                          <div style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;text-align: justify; padding: 0 10px; display: block;">
                            <p style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">Having doubts about what to wear to the occasion? The good news is, there is no dress code! But you still got to look good for the camera and dress to season.</p>
                          </div>
                        </td>
                      </tr>
                    </table>
                    <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;border-spacing:0 ;border-collapse:collapse ;table-layout:fixed ;margin:0 auto ;">
                      <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                        <td valign="middle" width="30%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;">
                          <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;border-spacing:0 ;border-collapse:collapse ;table-layout:fixed ;margin:0 auto ;">
                            <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                              <td align="right" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;">
                                <img src="https://raw.githubusercontent.com/arunsub-pvt/hjgufj887/master/images/suit-up.png" alt="" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;-ms-interpolation-mode:bicubic;width: 100%; max-width: 125px; height: auto; margin: 0; display: block;">
                              </td>
                            </tr>
                          </table>
                        </td>
                        <td valign="middle" width="70%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;">
                          <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;border-spacing:0 ;border-collapse:collapse ;table-layout:fixed ;margin:0 auto ;">
                            <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                              <td style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;padding-top: 20px; padding-left: 10px;">
                                <div class="heading-section" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;text-align: justify; padding: 0 20px;">
                                  <p style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">Gentlemen, this should go without saying - SUIT UP! Find the lightest coloured suit in your wardrobe that screams "SUMMER!". If you're going shopping or just need some ideas, take a look at this <a href="https://www.fashionbeans.com/2013/dressing-for-a-summer-wedding-guest/" target="_blank" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;text-decoration:none;color:#0d0cb5;">article</a> for inspiration!</p>
                                </div>
                              </td>
                            </tr>
                          </table>
                        </td>
                      </tr>
                    </table>
                    <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;border-spacing:0 ;border-collapse:collapse ;table-layout:fixed ;margin:0 auto ;">
                      <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                        <td valign="middle" width="70%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;">
                          <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;border-spacing:0 ;border-collapse:collapse ;table-layout:fixed ;margin:0 auto ;">
                            <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                              <td style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;padding-top: 20px;">
                                <div class="heading-section" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;text-align: justify; padding: 0 20px;">
                                  <p style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">Ladies, things are a lot easier for you compared to us men! The theme of the wedding is Indian. So indeed, Indian dresses are welcome! Otherwise go for a light summer evening dress that matches your date.</p>
                                </div>
                              </td>
                            </tr>
                          </table>
                        </td>
                        <td valign="middle" width="30%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;">
                          <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;border-spacing:0 ;border-collapse:collapse ;table-layout:fixed ;margin:0 auto ;">
                            <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                              <td style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;padding-top: 20px; padding-right: 10px; align: center;">
                                <img src="https://raw.githubusercontent.com/arunsub-pvt/hjgufj887/master/images/police.png" alt="" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;-ms-interpolation-mode:bicubic;text-align: right; height: 150px; max-height: 150px; width: auto; padding-right: 20px;">
                              </td>
                            </tr>
                          </table>
                        </td>
                      </tr>
                    </table>
                    <table style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;border-spacing:0 ;border-collapse:collapse ;table-layout:fixed ;margin:0 auto ;">
                      <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                        <td style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;">
                          <div style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;text-align: left; padding: 0 20px; display: block;">
                            <p style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;"><i style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;"><b style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">PS:</b> Follow the weather updates from 2-3 days before Saturday so you're better prepared!</i></p>
                          </div>
                        </td>
                      </tr>
                    </table>
                  </td>
                </tr>
                <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                  <td valign="middle" class="counter" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;width:100%;position:relative;z-index:0;mso-table-lspace:0pt ;mso-table-rspace:0pt ;background-image: url(https://raw.githubusercontent.com/arunsub-pvt/hjgufj887/master/images/wedding-gifts.jpeg); background-size: cover; padding: 4em 0;">
                    <div class="overlay" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;position:absolute;top:0;left:0;right:0;bottom:0;content:'';width:100%;background:#000000;z-index:-1;opacity:.3;"></div>
                    <table style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;border-spacing:0 ;border-collapse:collapse ;table-layout:fixed ;margin:0 auto ;">
                      <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                        <td valign="middle" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;">
                          <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;border-spacing:0 ;border-collapse:collapse ;table-layout:fixed ;margin:0 auto ;">
                            <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                              <div class="heading-section-white" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;color:rgba(255, 255, 255, .8);text-align: center; padding-top: 20px;">
                                <h2 style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;font-family:'Poppins', sans-serif;color:#000000;margin-top:0;font-family:line-height: 1;padding-bottom:0;color:#ffffff;margin-block-end: 0;">WHAT TO GIFT THE COUPLE?</h2>
                              </div>
                            </tr>
                          </table>
                        </td>
                      </tr>
                    </table>
                  </td>
                </tr>
                <!-- end: tr -->
                <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                  <td class="bg_white email-section" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;background:#ffffff;padding:2.5em;mso-table-lspace:0pt ;mso-table-rspace:0pt ;">
                    <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;border-spacing:0 ;border-collapse:collapse ;table-layout:fixed ;margin:0 auto ;">
                      <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                        <td valign="middle" width="30%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;">
                          <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;border-spacing:0 ;border-collapse:collapse ;table-layout:fixed ;margin:0 auto ;">
                            <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                              <td align="center" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;">
                                <img src="https://raw.githubusercontent.com/arunsub-pvt/hjgufj887/master/images/gift.png" alt="" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;-ms-interpolation-mode:bicubic;width: 100%; max-width: 200px; height: auto; margin: 0; display: block;">
                              </td>
                            </tr>
                          </table>
                        </td>
                      </tr>
                    </table>
                    <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;border-spacing:0 ;border-collapse:collapse ;table-layout:fixed ;margin:0 auto ;">
                      <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                        <td valign="middle" width="70%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;">
                          <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;border-spacing:0 ;border-collapse:collapse ;table-layout:fixed ;margin:0 auto ;">
                            <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                              <td style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;padding-top: 20px;">
                                <div class="heading-section" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;text-align: justify; padding: 0 10px;">
                                  <p style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">One of the best inspirations for picking a gift is considering the bride's and groom's life together ahead. Household and kitchen articles are popular choices. Since the couple loves travelling, you can also think of travel vouchers and gift cards. For more inspiration, check out this <a href="https://www.theperfectwedding.nl/artikelen/86/originele-huwelijkscadeaus" target="_blank" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;text-decoration:none;color:#0d0cb5;">article</a> (Sorry! It's in Dutch). At Dutch weddings, cash is also a popular wedding gift choice. On how much to give, you can consult this <a href="https://www.theperfectwedding.nl/artikelen/4330/hoeveel-geld-geef-bruiloft" target="_blank" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;text-decoration:none;color:#0d0cb5;">article</a> (Sorry again!). <br style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                                    If you know Harshitha and/or Phani very well, there is no time like this to surprise them with something personalised too!</p>
                                </div>
                              </td>
                            </tr>
                          </table>
                        </td>
                      </tr>
                    </table>
                  </td>
                </tr>
                <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                  <td valign="middle" class="counter" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;width:100%;position:relative;z-index:0;mso-table-lspace:0pt ;mso-table-rspace:0pt ;background-image: url(https://raw.githubusercontent.com/arunsub-pvt/hjgufj887/master/images/perform.jpg); background-size: cover; padding: 4em 0;">
                    <div class="overlay" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;position:absolute;top:0;left:0;right:0;bottom:0;content:'';width:100%;background:#000000;z-index:-1;opacity:.3;"></div>
                    <table style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;border-spacing:0 ;border-collapse:collapse ;table-layout:fixed ;margin:0 auto ;">
                      <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                        <td valign="middle" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;">
                          <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;border-spacing:0 ;border-collapse:collapse ;table-layout:fixed ;margin:0 auto ;">
                            <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                              <div class="heading-section-white" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;color:rgba(255, 255, 255, .8);text-align: center; padding-top: 20px;">
                                <h2 style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;font-family:'Poppins', sans-serif;color:#000000;margin-top:0;font-family:line-height: 1;padding-bottom:0;color:#ffffff;margin-block-end: 0;">I WANT TO PERFORM!</h2>
                              </div>
                            </tr>
                          </table>
                        </td>
                      </tr>
                    </table>
                  </td>
                </tr>
                <!-- end: tr -->
                <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                  <td class="bg_white email-section" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;background:#ffffff;padding:2.5em;mso-table-lspace:0pt ;mso-table-rspace:0pt ;">
                    <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;border-spacing:0 ;border-collapse:collapse ;table-layout:fixed ;margin:0 auto ;">
                      <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                        <td valign="middle" width="30%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;">
                          <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;border-spacing:0 ;border-collapse:collapse ;table-layout:fixed ;margin:0 auto ;">
                            <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                              <td align="center" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;">
                                <img src="https://raw.githubusercontent.com/arunsub-pvt/hjgufj887/master/images/sing.png" alt="" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;-ms-interpolation-mode:bicubic;width: 100%; max-width: 250px; height: auto; margin: 0;">
                                <img src="https://raw.githubusercontent.com/arunsub-pvt/hjgufj887/master/images/dance.png" alt="" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;-ms-interpolation-mode:bicubic;width: 100%; max-width: 250px; height: auto; margin: 0;">
                              </td>
                            </tr>
                          </table>
                        </td>
                      </tr>
                    </table>
                    <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;border-spacing:0 ;border-collapse:collapse ;table-layout:fixed ;margin:0 auto ;">
                      <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                        <td valign="middle" width="70%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;">
                          <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;border-spacing:0 ;border-collapse:collapse ;table-layout:fixed ;margin:0 auto ;">
                            <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                              <td style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt ;mso-table-rspace:0pt ;padding-top: 20px; padding-left: 10px;">
                                <div class="heading-section" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;text-align: justify; padding: 0 20px;">
                                  <p style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">Yes, you can! If you'd like to perform for the couple and couldn't make your mind up in time for the RSVP, simply reply to this e-mail with your request and I'll accommodate your wish in the schedule. If you need something arranged before hand, please let me know that too!</p>
                                </div>
                              </td>
                            </tr>
                          </table>
                        </td>
                      </tr>
                    </table>
                  </td>
                </tr>
                <!-- end: tr -->
                <tr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                  <td class="bg_light email-section" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;background:#fafafa;padding:2.5em;mso-table-lspace:0pt ;mso-table-rspace:0pt ;text-align:center;">
                    <div class="heading-section" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                      <h2 style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;font-family:'Poppins', sans-serif;color:#000000;font-size:20px;margin-top:0;line-height:1.4;font-weight:700;text-transform:uppercase;">That's all for now!</h2>
                      <p style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">If there are any updates, I will forward them via e-mail to you! Similarly, please let me know if you have any questions or doubts about the wedding itself by responding to this e-mail.
										<br style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                        Looking forward to seeing you at the wedding.</p>
                      <div style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;text-align: right;">
                        Cheers,<br style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;">
                        Arun
										</div>
                      <img src="https://raw.githubusercontent.com/arunsub-pvt/hjgufj887/master/images/bye.png" alt="" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;-ms-interpolation-mode:bicubic;width: 100%; max-width: 250px; height: auto; margin: 0;">
                    </div>
                  </td>
                </tr>
                <!-- end: tr -->
              </table>
            </td>
          </tr>
          <!-- end:tr -->
          <!-- 1 Column Text + Button : END -->
        </table>
      </div>
    </center>
  </body>
</html>
    """

    html = html.replace("_$$$_", recepient)

    message = MIMEMultipart("alternative")
    message["Subject"] = "Before the wedding..."
    message["From"] = sender_email
    message["To"] = receiver_email

    # Turn these into plain/html MIMEText objects
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )


mailer_list = {"i.arun.subramanian@gmail.com" : "Arun",
               "Abhimanyuselvan@gmail.com" : "Abhi & Pinky",
               "adithya.pulli@gmail.com" : "Adi & Suma",
               "antygan@gmail.com" : "Ananatha & Ankita",
               "talwar.avii@gmail.com" : "Jatin & Sonja",
               "bommareddy.kh@gmail.com" : "Harshini & Varun",
               "Phani.p3@gmail.com" : "Pawan",
               "r.kpooja12@gmail.com" : "Pooja",
               "rajeevbreddy@gmail.com" : "Rajeev & Pooja",
               "sumedh105@gmail.com" : "Sumedh & Ketki",
               "vg.karunanithi@gmail.com" : "Vikku, Vidhya & Mrudu",
               "vik1124@gmail.com" : "Vikram",
               "vishu991@gmail.com" : "Vishu & Sneha",
               "vladmihaisima@gmail.com" : "Vlad-Mihai & Alexandra",
               "sachin.singare@gmail.com" : "Sachin",
               "mcakshar.2351@gmail.com" : "Akshar"
               }

for e, r in mailer_list.items():
    sendmail(r, e)
