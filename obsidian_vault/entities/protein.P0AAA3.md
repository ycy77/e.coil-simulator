---
entity_id: "protein.P0AAA3"
entity_type: "protein"
name: "ecpA"
source_database: "UniProt"
source_id: "P0AAA3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Fimbrium {ECO:0000250}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ecpA matB yagZ b0293 JW0287"
---

# ecpA

`protein.P0AAA3`

## Static

- Type: `protein`
- Source: `UniProt:P0AAA3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Fimbrium {ECO:0000250}.

## Enriched Summary

FUNCTION: Part of the ecpRABCDE operon, which encodes the E.coli common pilus (ECP). ECP is found in both commensal and pathogenic strains and plays a dual role in early-stage biofilm development and host cell recognition. Major subunit of the fimbria (By similarity). {ECO:0000250}. EcpA (formerly MatB) is the major structural component of the E.coli common pilus (ECP) that is expressed in pathogenic E. coli strains at low temperatures . ECP are not expressed in E. coli K-12 . ecpA from E.coli K-12 MG1655 has 97.8% sequence identity with ecpA from the pathogenic isolate O18acK1H7 . Overexpression of the cloned E. coli K-12 MG1655 ecpABCDE genes in wild type E. coli K12 MG1655 results in ECP expression at 20oC and 37oC and biofilm formation at 20oC indicating that the genes are functional in E. coli MG1655 but are not expressed . ecpA (matB) is highly conserved in the genomes of E. coli strains, and most pathogenic strains of E. coli produce an ECP encoded by ecpA . E. coli K-12 contains 12 chaperone-usher fimbrial operons, including ecpABCDE; a fimbria-lacking mutant - strain WQM026 - created by deleting all 12 operons has been characterised EcpA: "E. coli common pilus" MatB: "meningitis-associated and temperature regulated"

## Annotation

FUNCTION: Part of the ecpRABCDE operon, which encodes the E.coli common pilus (ECP). ECP is found in both commensal and pathogenic strains and plays a dual role in early-stage biofilm development and host cell recognition. Major subunit of the fimbria (By similarity). {ECO:0000250}.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b0293|gene.b0293]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AAA3`
- `KEGG:ecj:JW0287;eco:b0293;ecoc:C3026_01430;ecoc:C3026_24060;`
- `GeneID:75204620;948759;`
- `GO:GO:0009289`

## Notes

Common pilus major fimbrillin subunit EcpA (MatB fimbrillin)
