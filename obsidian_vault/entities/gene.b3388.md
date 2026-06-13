---
entity_id: "gene.b3388"
entity_type: "gene"
name: "damX"
source_database: "NCBI RefSeq"
source_id: "gene-b3388"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3388"
  - "damX"
---

# damX

`gene.b3388`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3388`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

damX (gene.b3388) is a gene entity. It encodes damX (protein.P11557). Encoded protein function: FUNCTION: Non-essential cell division protein. {ECO:0000255|HAMAP-Rule:MF_02021, ECO:0000269|PubMed:19684127, ECO:0000269|PubMed:19880599}. EcoCyc product frame: EG11183-MONOMER. EcoCyc synonyms: yhfB. Genomic coordinates: 3516020-3517306. EcoCyc protein note: DamX is a non-essential cell division protein; it contains a C-terminal SPOR domain which targets the protein to the septal ring . Recruitment of DamX to the division site is dependent on EG10347-MONOMER, but not dependent on any other cell division protein tested . The SPOR domain is important for in vivo activities of DamX . In the uropathogenic E. coli strain UTI89, DamX was shown to be required for reversible filamentation and establishment of a urinary tract infection . DamX interacts directly with itself, EG10342-MONOMER and EG11529-MONOMER, and more weakly with other cell division proteins; its SPOR domain binds peptidoglycan . DamX also interacts with EG10605-MONOMER PBP1B and stimulates its glycosyltransferase activity . Relatively high binding affinity (Kd ~1 µM) of the SPOR domain to denuded glycans in E. coli sacculi was measured and found to be necessary for full function of DamX . DamX is predicted to be a bitopic inner membrane protein . A solution structure of the SPOR domain has been solved...

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P11557|protein.P11557]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=damX; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011065,ECOCYC:EG11183,GeneID:947930`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3516020-3517306:-; feature_type=gene
