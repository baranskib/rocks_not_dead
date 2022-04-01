resource "aws_cloudwatch_event_rule" "every_week" {
  name = "every-week"
  description = "Sends a trigger every week"
  schedule_expression = "rate(7 days)"
  is_enabled = false
}

resource "aws_cloudwatch_event_target" "trigger_cmo_strategy" {
  rule = "${aws_cloudwatch_event_rule.every_week.name}"
  target_id = "rocks_not_dead"
  arn = "${aws_lambda_function.rocks_not_dead.arn}"
}