import React, { useState } from 'react';
import axios from 'axios';
import {Box, Button, Container, Heading, Input, Textarea, VStack, FormControl, FormLabel, Text,} from '@chakra-ui/react';

function App() {
  const [numTestOutput, setNumTestOutput] = useState('');
  const [objective, setObjective] = useState('');
  const [output, setOutput] = useState('');
  const [generatedPrompt, setGeneratedPrompt] = useState(null);
  const [query, setQuery] = useState('');
  const [userMessage, setUserMessage] = useState('');
  const [evaluationResult, setEvaluationResult] = useState(null);

  const handleGeneratePrompts = async () => {
    try {
      const response = await axios.post('http://localhost:8000/generate_prompts/', {
          num_test_output: numTestOutput,
          objective: objective,
          output: output
      });
      setGeneratedPrompt(response.data);
  } catch (error) {
      console.error('Error generating prompt:', error);
  }
};

  const handleEvaluatePrompts = async () => {
    try {
      const response = await axios.post('http://localhost:8000/evaluate_prompts/', {
          query: query,
          user_message: userMessage
      });
      setEvaluationResult(response.data);
  } catch (error) {
      console.error('Error evaluating prompt:', error);
  }
};

return (
    <Container maxW="container.md" py={10}>
        <VStack spacing={10}>
            <Box w="100%">
                <Heading mb={5}>Prompt Generation and Evaluation</Heading>
                <Box p={5} shadow="md" borderWidth="1px">
                    <Heading size="md" mb={4}>Generate Prompt</Heading>
                    <VStack spacing={4}>
                        <FormControl id="numTestOutput">
                            <FormLabel>Num Test Output</FormLabel>
                            <Input type="text" value={numTestOutput} onChange={(e) => setNumTestOutput(e.target.value)} />
                        </FormControl>
                        <FormControl id="objective">
                            <FormLabel>Objective</FormLabel>
                            <Input type="text" value={objective} onChange={(e) => setObjective(e.target.value)} />
                        </FormControl>
                        <FormControl id="output">
                            <FormLabel>Output</FormLabel>
                            <Input type="text" value={output} onChange={(e) => setOutput(e.target.value)} />
                        </FormControl>
                        <Button colorScheme="teal" onClick={handleGeneratePrompts}>Generate</Button>
                        {generatedPrompt && (
                            <Box p={5} shadow="md" borderWidth="1px" w="100%">
                                <Heading size="sm">Generated Prompt</Heading>
                                <Text>Prompt: {generatedPrompt.prompt}</Text>
                                <Text>Score: {generatedPrompt.score}</Text>
                            </Box>
                        )}
                    </VStack>
                </Box>
            </Box>
            <Box w="100%">
                <Box p={5} shadow="md" borderWidth="1px">
                    <Heading size="md" mb={4}>Evaluate Prompt</Heading>
                    <VStack spacing={4}>
                        <FormControl id="query">
                            <FormLabel>Query</FormLabel>
                            <Input type="text" value={query} onChange={(e) => setQuery(e.target.value)} />
                        </FormControl>
                        <FormControl id="userMessage">
                            <FormLabel>User Message</FormLabel>
                            <Input type="text" value={userMessage} onChange={(e) => setUserMessage(e.target.value)} />
                        </FormControl>
                        <Button colorScheme="teal" onClick={handleEvaluatePrompts}>Evaluate</Button>
                        {evaluationResult && (
                            <Box p={5} shadow="md" borderWidth="1px" w="100%">
                                <Heading size="sm">Evaluation Result</Heading>
                                <Text>Result: {evaluationResult.result}</Text>
                            </Box>
                        )}
                    </VStack>
                </Box>
            </Box>
        </VStack>
    </Container>

);
}


export default App;

