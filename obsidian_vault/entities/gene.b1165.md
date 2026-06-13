---
entity_id: "gene.b1165"
entity_type: "gene"
name: "ymgA"
source_database: "NCBI RefSeq"
source_id: "gene-b1165"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1165"
  - "ymgA"
---

# ymgA

`gene.b1165`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1165`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ymgA (gene.b1165) is a gene entity. It encodes ymgA (protein.P75992). Encoded protein function: FUNCTION: Probably a connector protein for RcsB/C regulation of biofilm formation, providing additional signal input into the two-component signaling pathway. May serve to stimulate biofilm maturation, probably via the Rcs phosphorelay. Mild overexpression at 16 degrees Celsius increases the production of colanic acid, an exopolysaccharide and matrix component, and reduces adhesive curli fimbriae expression. Both of these effects require RcsB. EcoCyc product frame: G6605-MONOMER. Genomic coordinates: 1216068-1216340. EcoCyc protein note: Deletion of ymgA increases biofilm formation and motility . When placed on a low copy number plasmid at low temperature, ymgA increases production of capsule material and reduces expression of curli . Expression of ymgA is regulated under conditions of biofilm formation. The presence of AI-2 or the stationary phase biofilm signal indole repress ymgA expression. ymgA is repressed in young and mature biofilms, but is induced in the intermediate, developed biofilms , by rapid acid treatment and under low temperature growth conditions . Expression of ymgA is regulated by the repressor BluR and the alternative sigma factor RpoS as well as by MarA .

## Biological Role

Repressed by bluR (protein.P75989). Activated by rpoD (protein.P00579), marA (protein.P0ACH5), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75992|protein.P75992]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ymgA; function=+
- `activates` <-- [[protein.P0ACH5|protein.P0ACH5]] `RegulonDB` `C` - regulator=MarA; target=ymgA; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=ymgA; function=+
- `represses` <-- [[protein.P75989|protein.P75989]] `RegulonDB` `C` - regulator=BluR; target=ymgA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003909,ECOCYC:G6605,GeneID:948991`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1216068-1216340:+; feature_type=gene
