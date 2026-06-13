---
entity_id: "gene.b0041"
entity_type: "gene"
name: "fixA"
source_database: "NCBI RefSeq"
source_id: "gene-b0041"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0041"
  - "fixA"
---

# fixA

`gene.b0041`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0041`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fixA (gene.b0041) is a gene entity. It encodes fixA (protein.P60566). Encoded protein function: FUNCTION: Required for anaerobic carnitine reduction. May bring reductant to CaiA. {ECO:0000269|PubMed:12081978}. EcoCyc product frame: EG11562-MONOMER. EcoCyc synonyms: yaaQ. Genomic coordinates: 42403-43173. EcoCyc protein note: FixA and FixB are required for anaerobic carnitine reduction and are proposed to act in the transfer of electrons to crotonobetainyl-CoA reductase (CaiA) . FixA and FixB have similarity to mammalian electron transfer flavoprotein subunits (ETF-β and α families, respectively) and were predicted to play an electron transport role in E. coli based on sequence similarity . fixA, fixB, ydiQ, ydiR, ygcR, and ygcQ form a subsystem based on genome context methods, and may represent a previously uncharacterized electron transfer pathway . A fixA or fixB mutant exhibits a defect in anaerobic reduction of carnitine to γ-butyrobetaine . Chromosomal insertion mutants in fix genes have a growth defect under anaerobic conditions . The cai and fix operons are divergently transcribed in a coordinated fashion . The fix operon is expressed under anaerobic conditions in the presence of carnitine or crotonobetaine . Work by was performed with genes from E...

## Biological Role

Activated by rpoD (protein.P00579), caiF (protein.P0AE58).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P60566|protein.P60566]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=fixA; function=+
- `activates` <-- [[protein.P0AE58|protein.P0AE58]] `RegulonDB` `S` - regulator=CaiF; target=fixA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000145,ECOCYC:EG11562,GeneID:947316`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:42403-43173:+; feature_type=gene
