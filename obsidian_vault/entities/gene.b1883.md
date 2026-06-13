---
entity_id: "gene.b1883"
entity_type: "gene"
name: "cheB"
source_database: "NCBI RefSeq"
source_id: "gene-b1883"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1883"
  - "cheB"
---

# cheB

`gene.b1883`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1883`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cheB (gene.b1883) is a gene entity. It encodes cheB (protein.P07330). Encoded protein function: FUNCTION: Involved in chemotaxis (PubMed:2188960, PubMed:324984, PubMed:358191, PubMed:392505). Part of a chemotaxis signal transduction system that modulates chemotaxis in response to various stimuli (PubMed:2188960, PubMed:392505). Catalyzes the demethylation of specific methylglutamate residues introduced into the chemoreceptors (methyl-accepting chemotaxis proteins or MCP) by CheR (PubMed:2188960, PubMed:358191, PubMed:392505). Also mediates the irreversible deamidation of specific glutamine residues to glutamic acid (PubMed:6300110, PubMed:6304723). Catalyzes its own deactivation by removing the activating phosphoryl group (PubMed:2188960). {ECO:0000269|PubMed:2188960, ECO:0000269|PubMed:324984, ECO:0000269|PubMed:358191, ECO:0000269|PubMed:392505, ECO:0000269|PubMed:6300110, ECO:0000269|PubMed:6304723}. EcoCyc product frame: PHOSPHO-CHEB. Genomic coordinates: 1967452-1968501. EcoCyc protein note: This is the Asp56 phosphorylated form of the chemotaxis response regulator CheB...

## Biological Role

Activated by fliA (protein.P0AEM6).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P07330|protein.P07330]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AEM6|protein.P0AEM6]] `RegulonDB` `S` - sigma=sigma28; target=cheB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006284,ECOCYC:EG10147,GeneID:946394`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1967452-1968501:-; feature_type=gene
