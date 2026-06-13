---
entity_id: "gene.b2316"
entity_type: "gene"
name: "accD"
source_database: "NCBI RefSeq"
source_id: "gene-b2316"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2316"
  - "accD"
---

# accD

`gene.b2316`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2316`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

accD (gene.b2316) is a gene entity. It encodes accD (protein.P0A9Q5). Encoded protein function: FUNCTION: Component of the acetyl coenzyme A carboxylase (ACC) complex. Biotin carboxylase (BC) catalyzes the carboxylation of biotin on its carrier protein (BCCP) and then the CO(2) group is transferred by the transcarboxylase to acetyl-CoA to form malonyl-CoA.; FUNCTION: Controls translation of mRNA for both itself and the alpha-subunit (accA) by binding to a probable hairpin in the 5' of the mRNA. Binding to mRNA inhibits translation; this is partially relieved by acetyl-CoA. Increasing amounts of mRNA also inhibit enzyme activity. EcoCyc product frame: CARBOXYL-TRANSFERASE-BETA-MONOMER. EcoCyc synonyms: dedB, usg. Genomic coordinates: 2433012-2433926. EcoCyc protein note: The Zn2+-binding domain of AccD is required both for catalytic activity and for binding to mRNA . Transcription of accD is growth rate-regulated . A temperature-sensitive mutation in this gene was identified that showed potential as a growth-switch for genetic engineering . A lesson in gene naming:DedB: "downstream E. coli DNA (from hisT)" Usg: "upstream gene" AccD: "acetyl-CoA carboxylase D"

## Biological Role

Activated by rpoD (protein.P00579), fadR (protein.P0A8V6).

## Enriched Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9Q5|protein.P0A9Q5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=accD; function=+
- `activates` <-- [[protein.P0A8V6|protein.P0A8V6]] `RegulonDB` `S` - regulator=FadR; target=accD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007648,ECOCYC:EG10217,GeneID:946796`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2433012-2433926:-; feature_type=gene
