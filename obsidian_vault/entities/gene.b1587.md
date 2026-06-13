---
entity_id: "gene.b1587"
entity_type: "gene"
name: "ynfE"
source_database: "NCBI RefSeq"
source_id: "gene-b1587"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1587"
  - "ynfE"
---

# ynfE

`gene.b1587`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1587`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ynfE (gene.b1587) is a gene entity. It encodes ynfE (protein.P77374). Encoded protein function: FUNCTION: Terminal reductase during anaerobic growth on various sulfoxide and N-oxide compounds. {ECO:0000250}. EcoCyc product frame: G6845-MONOMER. Genomic coordinates: 1658069-1660495. EcoCyc protein note: YnfE has been implicated as a Tat-dependent selenate reductase enzyme in E. coli. A ynfEF double null mutant is unable to reduce selenate to elemental selenium . The disruption is specific to the initial selenate reduction process since selenium production is restored when selenite is added to the growth medium . Production of either YnfE or YnfF from a plasmid restored the ability of the E. coli ynfEF double mutant to reduce selenate to selenium in vivo . YnfE is highly similar to DmsA, the catalytic subunit of the dimethyl sulfoxide reductase heterotrimer, and cross-reacts with an anti-DmsA antibody. The protein is poorly expressed. In a plasmid expression system, expression of YnfE appears to inhibit expression of YnfFGH . In a ΔtusA strain, expression of ynfE is decreased in mid-exponential phase and under aerobic conditions .

## Biological Role

Repressed by narL (protein.P0AF28), nac (protein.Q47005). Activated by rpoD (protein.P00579), fnr (protein.P0A9E5), rpoS (protein.P13445).

## Enriched Pathways

- `eco00450` Selenocompound metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77374|protein.P77374]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ynfE; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=ynfE; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=ynfE; function=+
- `represses` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `S` - regulator=NarL; target=ynfE; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ynfE; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005302,ECOCYC:G6845,GeneID:946135`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1658069-1660495:+; feature_type=gene
