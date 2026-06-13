---
entity_id: "gene.b2841"
entity_type: "gene"
name: "araE"
source_database: "NCBI RefSeq"
source_id: "gene-b2841"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2841"
  - "araE"
---

# araE

`gene.b2841`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2841`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

araE (gene.b2841) is a gene entity. It encodes araE (protein.P0AE24). Encoded protein function: FUNCTION: Uptake of L-arabinose across the cytoplasmic membrane with the concomitant transport of protons into the cell (symport system) (PubMed:2836407, PubMed:6282256, PubMed:7030324). D-fucose, a nonmetabolizable analog of L-arabinose, is also a good substrate (PubMed:6282256). {ECO:0000269|PubMed:2836407, ECO:0000269|PubMed:6282256, ECO:0000269|PubMed:7030324}. EcoCyc product frame: ARAE-MONOMER. Genomic coordinates: 2980764-2982182. EcoCyc protein note: AraE is an arabinose/proton symporter responsible for the uptake of arabinose. Studies in membrane vesicles have shown that AraE can transport L-arabinose with low affinity (140-320 μM) and arabinose transport is coupled with proton transport . The AraE protein has been overproduced and reconstituted in liposomes as an arabinose/proton symporter . AraE is a member of the major facilitator superfamily (MFS) of transporters . Arabinose is the sole inducer of araE expression , which is controlled by the AraC regulator. An inhibitory effect on araE induced by arabinose appeared in the presence of xylose . Imported arabinose is catabolized to xylulose-5-phosphatel, which then enters the pentose phosphate pathway.

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoD (protein.P00579), araC (protein.P0A9E0), crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AE24|protein.P0AE24]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=araE; function=+
- `activates` <-- [[protein.P0A9E0|protein.P0A9E0]] `RegulonDB` `S` - regulator=AraC; target=araE; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=araE; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=araE; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0009319,ECOCYC:EG10056,GeneID:947341`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2980764-2982182:-; feature_type=gene
