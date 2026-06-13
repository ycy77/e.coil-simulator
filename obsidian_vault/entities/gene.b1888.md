---
entity_id: "gene.b1888"
entity_type: "gene"
name: "cheA"
source_database: "NCBI RefSeq"
source_id: "gene-b1888"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1888"
  - "cheA"
---

# cheA

`gene.b1888`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1888`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cheA (gene.b1888) is a gene entity. It encodes cheA (protein.P07363). Encoded protein function: FUNCTION: Involved in the transmission of sensory signals from the chemoreceptors to the flagellar motors. CheA is autophosphorylated; it can transfer its phosphate group to either CheB or CheY. EcoCyc product frame: PROTEIN-CHEA. Genomic coordinates: 1973360-1975324. EcoCyc protein note: CheA is the histidine protein kinase of two-component signaling pathways (chemotaxis, thermotaxis and energy taxis) which respond to environmental cues and signal change to the flagellar switch complex to regulate swimming behavior. CheA forms ternary signaling complexes with chemoreceptor proteins (CPLX0-8103 "Tsr", CPLX0-8102 "Tar", CPLX0-8105 "Trg" and CPLX0-8104 "Tap") and the coupling protein CHEW-MONOMER "CheW"; ligand binding to the receptor proteins generates a signal that is transmitted across the inner membrane to regulate CheA histidine kinase activity and the subsequent flow of phosphoryl groups to the response regulators CHEY-MONOMER "CheY" - whose phosphorylation status regulates the direction of flagellar motor rotation - and CHEB-MONOMER "CheB" - a protein glutamate methylesterase which modulates the sensory adaption system (see reviews )...

## Biological Role

Repressed by cpxR (protein.P0AE88). Activated by nac (protein.Q47005).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Pathways

- `eco02020` Two-component system (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)

## Outgoing Edges (1)

- `encodes` --> [[protein.P07363|protein.P07363]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=cheA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0AE88|protein.P0AE88]] `RegulonDB` `S` - regulator=CpxR; target=cheA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0006294,ECOCYC:EG10146,GeneID:946401`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1973360-1975324:-; feature_type=gene
