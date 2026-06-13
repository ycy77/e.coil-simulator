---
entity_id: "gene.b3974"
entity_type: "gene"
name: "coaA"
source_database: "NCBI RefSeq"
source_id: "gene-b3974"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3974"
  - "coaA"
---

# coaA

`gene.b3974`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3974`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

coaA (gene.b3974) is a gene entity. It encodes coaA (protein.P0A6I3). Encoded protein function: Pantothenate kinase (EC 2.7.1.33) (Pantothenic acid kinase) (Rts protein) EcoCyc product frame: PANTOTHENATE-KIN-MONOMER. EcoCyc synonyms: panK, rts, ts-9. Genomic coordinates: 4174076-4175026. EcoCyc protein note: Pantothenate kinase catalyzes the first step in the biosynthesis of coenzyme A, an essential cofactor that is involved in many reactions. This reaction is also the most highly regulated step in the pathway . Pantothenate kinase is sensitive to feedback inhibition by the CoA pool . Mutants that are refractory to feedback inhibition, but retain catalytic activity, have been isolated; these mutants have a higher intracellular CoA content and secrete 4'-phosphopantetheine . The compounds CPD0-1152 and CPD0-1153 are competitive inhibitors of pantothenate kinase and can be utilized as substrates of the CoA biosynthesis pathway . The phosphopantothenimide moiety is transferred to ACP, rendering it incapable of supporting fatty acid biosynthesis. Thus, CPD0-1152 and CPD0-1153 are pro-antibiotics , explaining earlier results . Further inhibitors/substrates of pantothenate kinase have been designed and tested . Growth rescue of a EG10004 dfp null mutant by addition of pantethine requires the pantetheine kinase activity of CoaA...

## Enriched Pathways

- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6I3|protein.P0A6I3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0013003,ECOCYC:EG10922,GeneID:948479`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4174076-4175026:-; feature_type=gene
