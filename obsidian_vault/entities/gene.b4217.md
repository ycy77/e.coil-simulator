---
entity_id: "gene.b4217"
entity_type: "gene"
name: "ytfK"
source_database: "NCBI RefSeq"
source_id: "gene-b4217"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4217"
  - "ytfK"
---

# ytfK

`gene.b4217`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4217`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ytfK (gene.b4217) is a gene entity. It encodes ytfK (protein.P0ADE2). Encoded protein function: Uncharacterized protein YtfK EcoCyc product frame: G7872-MONOMER. Genomic coordinates: 4439587-4439793. EcoCyc protein note: YtfK has been shown to play a role in the stringent response under phosphate and fatty acid starvation conditions. YtfK interacts with the catalytic domains of the bifunctional (p)ppGpp synthetase/hydrolase SPOT-MONOMER SpoT and may thus activate the stringent response by increasing SpoT's (p)ppGpp synthetase activity . During phosphate and fatty acid starvation, a ΔytfK mutant shows decreased accumulation of (p)ppGpp compared to wild type. A P42L mutant does not interact with SpoT and does not increase (p)ppGpp accumulation upon overexpression . YtfK appears to play a role in tolerance to H2O2 exposure and phosphate starvation . Expression of ytfK is activated by PhoB . YtfK levels are increased during phosphate and fatty acid starvation. Overexpression of ytfK suppresses the growth defect of a ΔrelA mutant on SMG medium; suppression is spoT-dependent .

## Biological Role

Repressed by lrp (protein.P0ACJ0), nac (protein.Q47005). Activated by crp (protein.P0ACJ8), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADE2|protein.P0ADE2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=ytfK; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=ytfK; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `S` - regulator=Lrp; target=ytfK; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ytfK; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013797,ECOCYC:G7872,GeneID:948736`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4439587-4439793:+; feature_type=gene
