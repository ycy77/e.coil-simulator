---
entity_id: "gene.b1887"
entity_type: "gene"
name: "cheW"
source_database: "NCBI RefSeq"
source_id: "gene-b1887"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1887"
  - "cheW"
---

# cheW

`gene.b1887`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1887`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cheW (gene.b1887) is a gene entity. It encodes cheW (protein.P0A964). Encoded protein function: FUNCTION: Involved in the transmission of sensory signals from the chemoreceptors to the flagellar motors. It physically bridges CheA to the MCPs (methyl-accepting chemotaxis proteins) to allow regulated phosphotransfer to CheY and CheB. EcoCyc product frame: CHEW-MONOMER. Genomic coordinates: 1972836-1973339. EcoCyc protein note: CheW is the coupling protein in the ternary receptor complexes of two-component signaling pathways (chemotaxis, thermotaxis and energy taxis) which respond to environmental cues (both external and internal) and signal change to the flagellar switch complex to regulate swimming behavior. CheW forms ternary signaling complexes with chemoreceptor proteins (CPLX0-8103 "Tsr", CPLX0-8102 "Tar", CPLX0-8105 "Trg" and CPLX0-8104 "Tap") and the protein histidine kinase CHEA-CPLX "CheA"; ligand binding to the receptor proteins generates a signal that is transmitted across the inner membrane to regulate CheA histidine kinase activity and the subsequent flow of phosphoryl groups to the response regulators CHEY-MONOMER "CheY" - whose phosphorylation status regulates the direction of flagellar motor rotation - and CHEB-MONOMER "CheB" - a protein glutamate methylesterase which modulates the sensory adaption system (see reviews )...

## Biological Role

Repressed by cpxR (protein.P0AE88).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A964|protein.P0A964]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0AE88|protein.P0AE88]] `RegulonDB` `S` - regulator=CpxR; target=cheW; function=-

## External IDs

- `Dbxref:ASAP:ABE-0006292,ECOCYC:EG10149,GeneID:946400`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1972836-1973339:-; feature_type=gene
