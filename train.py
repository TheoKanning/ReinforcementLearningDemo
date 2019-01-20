import manual_agent, rl_agent
import environment
import runner

if __name__ == '__main__':
  agent = rl_agent.RlAgent(4, 9, learning_rate=0.5)
  #agent = manual_agent.ManualAgent(4)
  environment = environment.Gridworld()
  runner = runner.Runner(agent, environment, num_iterations=1000)

  runner.run_experiment()
