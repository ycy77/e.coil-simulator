---
entity_id: "gene.b4150"
entity_type: "gene"
name: "ampC"
source_database: "NCBI RefSeq"
source_id: "gene-b4150"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4150"
  - "ampC"
---

# ampC

`gene.b4150`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4150`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ampC (gene.b4150) is a gene entity. It encodes ampC (protein.P00811). Encoded protein function: FUNCTION: Class C beta-lactamase which confers resistance to penicillins and cephalosporins (PubMed:12323371, PubMed:17956081, PubMed:23043117, PubMed:33199391, PubMed:6998377). Has benzylpenicillin- and cephaloridine-hydrolyzing activity (PubMed:3264154, PubMed:3264155, PubMed:6998377). Has weak cefuroxime, cefotaxime, cefoxitin and oxacillin-hydrolyzing activities (PubMed:19913034, PubMed:3264154, PubMed:3264155). {ECO:0000269|PubMed:12323371, ECO:0000269|PubMed:17956081, ECO:0000269|PubMed:19913034, ECO:0000269|PubMed:23043117, ECO:0000269|PubMed:3264154, ECO:0000269|PubMed:3264155, ECO:0000269|PubMed:33199391, ECO:0000269|PubMed:6998377}. EcoCyc product frame: EG10040-MONOMER. EcoCyc synonyms: ampA. Genomic coordinates: 4377811-4378944. EcoCyc protein note: The ampC β-lactamase gene encodes a serine cephalosporinase . AmpC was shown to be active against penicillin G with a Km of 12 μM, D-ampicillin with a Km of 6 μM, and cephalosporin C with a Km of 217 μM . AmpC has been shown to bind 125I-penicillin-X and aztreonam . AmpC is also believed to have an additional function as a peptidoglycan hydrolyzing enzyme . The ampA1 mutation, located in the promoter or operator region for ampC, causes increased expression of the ampC gene resulting in increased β-lactam resistance...

## Enriched Pathways

- `eco01501` beta-Lactam resistance (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P00811|protein.P00811]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0013592,ECOCYC:EG10040,GeneID:948669`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4377811-4378944:-; feature_type=gene
