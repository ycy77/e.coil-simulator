---
entity_id: "gene.b0970"
entity_type: "gene"
name: "yccA"
source_database: "NCBI RefSeq"
source_id: "gene-b0970"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0970"
  - "yccA"
---

# yccA

`gene.b0970`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0970`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yccA (gene.b0970) is a gene entity. It encodes yccA (protein.P0AAC6). Encoded protein function: FUNCTION: Negatively modulates the activity of the FtsH protease for membrane substrates. Overexpression or stabilizing YccA counteracts the FtsH-mediated degradation of SecY when the SecYEG preprotein translocator is jammed. {ECO:0000269|PubMed:19661432}. EcoCyc product frame: EG11113-MONOMER. Genomic coordinates: 1030759-1031418. EcoCyc protein note: YccA is a substrate of EG11506-MONOMER "FtsH" and a modulator of FtsH-mediated proteolysis . YccA is predicted to have seven membrane spanning regions . YccA is subject to FtsH-mediated proteolysis . The sequence determinants of protease recognition have been examined in detail . YccA interacts with FtsH and with the HflK-HflC (HflKC) complex, which modulates FtsH activity . The yccA11 mutation causes deletion of eight residues from the cytoplasmic N terminus; YccA11 mutant protein exhibits resistance to FtsH-mediated degradation and a yccA11 mutant strain exhibits selective defects in FtsH-mediated degradation, including a defect in degradation of free SecY protein . YccA11 mutant protein does not exhibit a defect in interaction with FtsH or with HflKC and HflKC is required for the SecY degradation defect of the yccA11 mutant...

## Biological Role

Activated by rpoD (protein.P00579), cpxR (protein.P0AE88).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAC6|protein.P0AAC6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=yccA; function=+
- `activates` <-- [[protein.P0AE88|protein.P0AE88]] `RegulonDB` `C` - regulator=CpxR; target=yccA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0003280,ECOCYC:EG11113,GeneID:946016`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1030759-1031418:-; feature_type=gene
