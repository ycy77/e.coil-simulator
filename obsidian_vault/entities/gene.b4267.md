---
entity_id: "gene.b4267"
entity_type: "gene"
name: "idnD"
source_database: "NCBI RefSeq"
source_id: "gene-b4267"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4267"
  - "idnD"
---

# idnD

`gene.b4267`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4267`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

idnD (gene.b4267) is a gene entity. It encodes idnD (protein.P39346). Encoded protein function: FUNCTION: Catalyzes the NADH/NADPH-dependent oxidation of L-idonate to 5-ketogluconate (5KG). {ECO:0000269|PubMed:9658018}. EcoCyc product frame: IDONDEHYD-MONOMER. EcoCyc synonyms: yjgV. Genomic coordinates: 4493375-4494406. EcoCyc protein note: L-idonate 5-dehydrogenase catalyzes the reversible oxidation of L-idonate to 5-ketogluconate. This is the first reaction of the L-idonate catabolic pathway after uptake of L-idonate into the cell. The enzyme specifically oxidizes L-idonate using NAD and catalyzes the specific reduction of 5-ketogluconate using NADH or NADPH . A strain containing a deletion of idnD can not grow on L-idonate as the sole source of carbon and energy . Expression of the idnDOTR operon is catabolite repressed and induced by L-idonate or 5-ketogluconate . IdnD: "idonate" Review:

## Biological Role

Activated by glaR (protein.P37338).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39346|protein.P39346]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=idnD; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013975,ECOCYC:G7893,GeneID:944769`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4493375-4494406:-; feature_type=gene
