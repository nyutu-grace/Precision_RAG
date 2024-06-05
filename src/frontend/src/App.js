import React, { useState } from 'react';
import { ChakraProvider, Box, VStack, Heading, Textarea, Button, FormControl, FormLabel, Spinner, Text } from '@chakra-ui/react';
import axios from 'axios';

function App() {
  const [query, setQuery] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);


  const handleSubmit = async () => {
    setLoading(true);
    setError(null);
    setResult(null);
    try {
      const response = await axios.post('http://localhost:8000/generate_prompts/', {
        query,
        });
      setResult(response.data);
    } catch (err) {
      setError('Failed to generate prompts. Please try again.');
    }
    setLoading(false);
  };

  return (
    <ChakraProvider>
      <Box maxW="800px" mx="auto" p={4}>
        <VStack spacing={4}>
          <Heading as="h1" size="xl" textAlign="center">Prompt Generator</Heading>
          <FormControl id="query">
            <FormLabel>Input your document or result</FormLabel>
            <Textarea
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="Enter your document or result here..."
              size="lg"
            />
          </FormControl>
          <Button colorScheme="teal" onClick={handleSubmit} isFullWidth>Generate Prompts</Button>
          {loading && <Spinner />}
          {error && <Text color="red.500">{error}</Text>}
          {result && (
            <Box w="100%" p={4} borderWidth={1} borderRadius="lg">
              <Heading as="h2" size="md">Generated Prompts</Heading>
              <Text mt={2}>{result.prompt}</Text>
            </Box>
          )}
        </VStack>
      </Box>
    </ChakraProvider>
  );
}

export default App;


