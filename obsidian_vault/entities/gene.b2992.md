---
entity_id: "gene.b2992"
entity_type: "gene"
name: "hybE"
source_database: "NCBI RefSeq"
source_id: "gene-b2992"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2992"
  - "hybE"
---

# hybE

`gene.b2992`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2992`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hybE (gene.b2992) is a gene entity. It encodes hybE (protein.P0AAN1). Encoded protein function: Hydrogenase-2 operon protein HybE EcoCyc product frame: EG11803-MONOMER. Genomic coordinates: 3140311-3140799. EcoCyc protein note: HybE plays a role in coordinating assembly and export of the FORMHYDROG2-CPLX subunits HybO and HybC. HybE physically interacts with Tat signal peptide-containing HybO and HybC precursor proteins, which are Tat export substrates. A solution structure of HybE shows that the protein adopts a three-layer sandwich fold with a disordered C-terminal region . A hybE deletion strain has very low hydrogenase 2 activity; in this strain, the HybO subunit is associated with the membrane, but HybC, although C-terminally processed, remains in the cytoplasm . Reviews:

## Biological Role

Repressed by yfeC (protein.P0AD37). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAN1|protein.P0AAN1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=hybE; function=+
- `represses` <-- [[protein.P0AD37|protein.P0AD37]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0009824,ECOCYC:EG11803,GeneID:947483`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3140311-3140799:-; feature_type=gene
