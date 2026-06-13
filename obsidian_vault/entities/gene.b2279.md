---
entity_id: "gene.b2279"
entity_type: "gene"
name: "nuoK"
source_database: "NCBI RefSeq"
source_id: "gene-b2279"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2279"
  - "nuoK"
---

# nuoK

`gene.b2279`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2279`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nuoK (gene.b2279) is a gene entity. It encodes nuoK (protein.P0AFE4). Encoded protein function: FUNCTION: NDH-1 shuttles electrons from NADH, via FMN and iron-sulfur (Fe-S) centers, to quinones in the respiratory chain. The immediate electron acceptor for the enzyme in this species is believed to be ubiquinone. Couples the redox reaction to proton translocation (for every two electrons transferred, four hydrogen ions are translocated across the cytoplasmic membrane), and thus conserves the redox energy in a proton gradient.; FUNCTION: There are 2 NADH dehydrogenases in E.coli, however only this complex is able to use dNADH (reduced nicotinamide hypoxanthine dinucleotide, deamino-NADH) and dNADH-DB (dimethoxy-5-methyl-6-decyl-1,4-benzoquinone) as substrates. EcoCyc product frame: NUOK-MONOMER. Genomic coordinates: 2395043-2395345. EcoCyc protein note: NuoK is part of the inner membrane component of NADH dehydrogenase I . The protein has three predicted transmembrane domains; the C terminus is located in the cytoplasm . A crystal structure of the membrane component at higher resolution has allowed better identification of the interactions between the subunits . NuoK participates in proton translocation . The SecYEG protein secretion machinery and its YidC component are required for insertion of NuoK in the cytoplasmic membrane...

## Biological Role

Repressed by ryhB (gene.b4451), fnr (protein.P0A9E5), arcA (protein.P0A9Q1). Activated by rpoD (protein.P00579), fis (protein.P0A6R3), cra (protein.P0ACP1).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFE4|protein.P0AFE4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=nuoK; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=nuoK; function=+
- `activates` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=nuoK; function=+
- `represses` <-- [[gene.b4451|gene.b4451]] `RegulonDB` `S` - regulator=RyhB; target=nuoK; function=-
- `represses` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=nuoK; function=-
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `C` - regulator=ArcA; target=nuoK; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007534,ECOCYC:EG12091,GeneID:947580`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2395043-2395345:-; feature_type=gene
