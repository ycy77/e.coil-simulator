---
entity_id: "gene.b3132"
entity_type: "gene"
name: "kbaZ"
source_database: "NCBI RefSeq"
source_id: "gene-b3132"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3132"
  - "kbaZ"
---

# kbaZ

`gene.b3132`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3132`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

kbaZ (gene.b3132) is a gene entity. It encodes kbaZ (protein.P0C8K0). Encoded protein function: FUNCTION: Component of the tagatose-1,6-bisphosphate aldolase KbaYZ that is required for full activity and stability of the Y subunit. Could have a chaperone-like function for the proper and stable folding of KbaY. When expressed alone, KbaZ does not show any aldolase activity. {ECO:0000269|PubMed:11976750}. EcoCyc product frame: G7631-MONOMER. EcoCyc synonyms: yhaX, agaZ. Genomic coordinates: 3278914-3280194. EcoCyc protein note: The KbaZ protein has no catalytic activity, but may stabilize the tagatose-1,6-bisphosphate aldolase CPLX0-240 KbaY. KbaZ appears to be required for full activity of KbaY, and thus may have a chaperone-like function . However like E. coli's other putative tagatose-1,6-bisphosphate aldolase chaperone G7128-MONOMER GatZ, structural analysis of KbaZ with AlphaFold and Rosetta predicted a structure with a Zn2+ cofactor and conserved amino acid residues in an active site that is structurally similar and mechanistically consistent with known C4 epimerases . Overexpression of kbaYZ has been shown to complement mutations to gatYZ . KbaZ is able to produce D-tagatose in the triple mutant ΔpfkAΔzwfΔgatZ when G7187-MONOMER is present to dephosphorylate D-tagatose-6-P to D-tagatose .

## Biological Role

Repressed by agaR (protein.P0ACK2). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0C8K0|protein.P0C8K0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=kbaZ; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=kbaZ; function=+
- `represses` <-- [[protein.P0ACK2|protein.P0ACK2]] `RegulonDB` `S` - regulator=AgaR; target=kbaZ; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010295,ECOCYC:G7631,GeneID:947637`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3278914-3280194:+; feature_type=gene
