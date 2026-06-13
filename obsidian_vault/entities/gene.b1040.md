---
entity_id: "gene.b1040"
entity_type: "gene"
name: "csgD"
source_database: "NCBI RefSeq"
source_id: "gene-b1040"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1040"
  - "csgD"
---

# csgD

`gene.b1040`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1040`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

csgD (gene.b1040) is a gene entity. It encodes csgD (protein.P52106). Encoded protein function: FUNCTION: The master regulator for adhesive curli fimbriae expression; necessary for transcription of the csgBAC/ymdA operon. Plays a positive role in biofilm formation. May have the capability to respond to starvation and/or high cell density by activating csgBA transcription. Low-level constitutive expression confers an adherent curli fimbriae-expressing phenotype, up-regulates 10 genes and down-regulates 14 others. {ECO:0000269|PubMed:16513732}. EcoCyc product frame: PD01379. Genomic coordinates: 1102546-1103196. EcoCyc protein note: The protein CsgD, for "Curlin subunit gene D," is a transcriptional regulator that regulates a number of genes involved in the Curli assembly, transport, and structural components , which are important for biofilm formation . CsgD was beneficial to biofilm formation in Salmonella Typhimurium, like in E. coli, after 48 h of growth . In addition, it also regulates genes related to cell surface-associated structures . It may also have the capability to respond to starvation and high cell density and positively controls σS expression . In general the environmental conditions, such as low osmolarity, low growth temperature (csgD and the production of the biofilm and cellulose...

## Biological Role

Repressed by rybB (gene.b4417), mcaS (gene.b4426), rprA (gene.b4431), omrA (gene.b4444), omrB (gene.b4445), hns (protein.P0ACF8), cpxR (protein.P0AE88), btsR (protein.P0AFT5), and 3 more. Activated by rpoD (protein.P00579), ompR (protein.P0AA16), cra (protein.P0ACP1), rpoS (protein.P13445), basR (protein.P30843), mlrA (protein.P33358), csgD (protein.P52106), rcdA (protein.P75811).

## Enriched Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P52106|protein.P52106]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (19)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=csgD; function=+
- `activates` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `C` - regulator=OmpR; target=csgD; function=+
- `activates` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=csgD; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=csgD; function=+
- `activates` <-- [[protein.P30843|protein.P30843]] `RegulonDB` `S` - regulator=BasR; target=csgD; function=+
- `activates` <-- [[protein.P33358|protein.P33358]] `RegulonDB` `S` - regulator=MlrA; target=csgD; function=+
- `activates` <-- [[protein.P52106|protein.P52106]] `RegulonDB` `S` - regulator=CsgD; target=csgD; function=+
- `activates` <-- [[protein.P75811|protein.P75811]] `RegulonDB` `S` - regulator=RcdA; target=csgD; function=+
- `represses` <-- [[gene.b4417|gene.b4417]] `RegulonDB` `S` - regulator=RybB; target=csgD; function=-
- `represses` <-- [[gene.b4426|gene.b4426]] `RegulonDB` `S` - regulator=McaS; target=csgD; function=-
- `represses` <-- [[gene.b4431|gene.b4431]] `RegulonDB` `S` - regulator=RprA; target=csgD; function=-
- `represses` <-- [[gene.b4444|gene.b4444]] `RegulonDB` `S` - regulator=OmrA; target=csgD; function=-
- `represses` <-- [[gene.b4445|gene.b4445]] `RegulonDB` `S` - regulator=OmrB; target=csgD; function=-
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=csgD; function=-
- `represses` <-- [[protein.P0AE88|protein.P0AE88]] `RegulonDB` `S` - regulator=CpxR; target=csgD; function=-
- `represses` <-- [[protein.P0AFT5|protein.P0AFT5]] `RegulonDB` `S` - regulator=BtsR; target=csgD; function=-
- `represses` <-- [[protein.P52108|protein.P52108]] `RegulonDB` `S` - regulator=RstA; target=csgD; function=-
- `represses` <-- [[protein.P52627|protein.P52627]] `RegulonDB` `S` - regulator=FliZ; target=csgD; function=-
- `represses` <-- [[protein.Q46864|protein.Q46864]] `RegulonDB` `S` - regulator=MqsA; target=csgD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003530,ECOCYC:G6546,GeneID:949119`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1102546-1103196:-; feature_type=gene
