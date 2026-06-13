---
entity_id: "gene.b1603"
entity_type: "gene"
name: "pntA"
source_database: "NCBI RefSeq"
source_id: "gene-b1603"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1603"
  - "pntA"
---

# pntA

`gene.b1603`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1603`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pntA (gene.b1603) is a gene entity. It encodes pntA (protein.P07001). Encoded protein function: FUNCTION: The transhydrogenation between NADH and NADP is coupled to respiration and ATP hydrolysis and functions as a proton pump across the membrane. {ECO:0000269|PubMed:16083909}. EcoCyc product frame: PNTA-MONOMER. Genomic coordinates: 1676371-1677903. EcoCyc protein note: pntA encodes the α subunit of membrane-bound proton-translocating pyridine nucleotide transhydrogenase. The α subunit is predicted to consist of a large N-terminal cytosolic region (domain I) which binds NAD(H) , followed by 4 transmembrane regions and a short C-terminal tail .

## Biological Role

Repressed by nac (protein.Q47005). Activated by arcA (protein.P0A9Q1), lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P07001|protein.P07001]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=pntA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=pntA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005354,ECOCYC:EG10744,GeneID:946628`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1676371-1677903:-; feature_type=gene
