---
entity_id: "gene.b4376"
entity_type: "gene"
name: "osmY"
source_database: "NCBI RefSeq"
source_id: "gene-b4376"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4376"
  - "osmY"
---

# osmY

`gene.b4376`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4376`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

osmY (gene.b4376) is a gene entity. It encodes osmY (protein.P0AFH8). Encoded protein function: Osmotically-inducible protein Y EcoCyc product frame: EG11391-MONOMER. EcoCyc synonyms: csi-5. Genomic coordinates: 4611396-4612001. EcoCyc protein note: OsmY is induced by hyperosmotic stress and during entry into stationary phase . osmY::TnphoA mutants show slightly increased sensitivity to hyperosmotic stress . OsmY confers a growth benefit at high osmolarity that is dependent on glycerol in the growth medium and the presence of CPLX0-7653 aquaporin Z . OsmY is a mobile, monomeric, periplasmic protein with two flexibly linked BON - bacterial OsmY and nodulation - domains (BON1 and BON2); the BON1 domain is required for growth at high osmolarity . OsmY is induced by stresses known to cause protein misfolding (see and references within). Overproduction of OsmY stabilises a highly unstable MBP mutant; purified OsmY inhibits the aggregation of lactate dehydrogenase, α-lactalbumin and, less effectively, luciferase . OsmY is very resistant to aggregation under a variety of denaturing conditions . OsmY is important for the assembly of G7080-MONOMER Ag43; purified OsmY promotes the refolding of the Ag43 β-barrel domain in vitro and protects it from digestion by exogenous proteases . OsmY affects Ag43 levels only in the absence of EG10985-MONOMER SurA...

## Biological Role

Repressed by arcA (protein.P0A9Q1), lrp (protein.P0ACJ0), fliZ (protein.P52627), nac (protein.Q47005). Activated by rpoD (protein.P00579), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFH8|protein.P0AFH8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=osmY; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=osmY; function=+
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=osmY; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `S` - regulator=Lrp; target=osmY; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P52627|protein.P52627]] `RegulonDB` `S` - regulator=FliZ; target=osmY; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=osmY; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0014348,ECOCYC:EG11391,GeneID:948895`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4611396-4612001:+; feature_type=gene
