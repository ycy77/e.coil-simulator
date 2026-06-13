---
entity_id: "gene.b2263"
entity_type: "gene"
name: "menH"
source_database: "NCBI RefSeq"
source_id: "gene-b2263"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2263"
  - "menH"
---

# menH

`gene.b2263`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2263`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

menH (gene.b2263) is a gene entity. It encodes menH (protein.P37355). Encoded protein function: FUNCTION: Catalyzes a proton abstraction reaction that results in 2,5-elimination of pyruvate from 2-succinyl-5-enolpyruvyl-6-hydroxy-3-cyclohexene-1-carboxylate (SEPHCHC) and the formation of 2-succinyl-6-hydroxy-2,4-cyclohexadiene-1-carboxylate (SHCHC). Is also able to catalyze the hydrolysis of the thioester bond in palmitoyl-CoA in vitro. {ECO:0000269|PubMed:15808744, ECO:0000269|PubMed:18284213}. EcoCyc product frame: EG12438-MONOMER. EcoCyc synonyms: yfbB. Genomic coordinates: 2376834-2377592. EcoCyc protein note: MenH catalyzes the third step in the menaquinone biosynthesis pathway, a proton abstraction reaction that results in 2,5-elimination of pyruvate from CPD-9924 and the formation of CPD-9923 . SHCHC synthase activity was first detected in crude extracts . Structural modelling and site-directed mutagenesis allowed identification of active site residues . Crystal structures of the wild type protein and two active site mutants have been solved . MenH was initially suggested to catalyze a thioesterase step in the menaquinone biosynthetic pathway . However, the purified protein lacks thioesterase activity, but has efficient SHCHC synthase activity...

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37355|protein.P37355]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007478,ECOCYC:EG12438,GeneID:946736`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2376834-2377592:-; feature_type=gene
