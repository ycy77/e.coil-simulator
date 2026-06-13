---
entity_id: "gene.b1038"
entity_type: "gene"
name: "csgF"
source_database: "NCBI RefSeq"
source_id: "gene-b1038"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1038"
  - "csgF"
---

# csgF

`gene.b1038`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1038`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

csgF (gene.b1038) is a gene entity. It encodes csgF (protein.P0AE98). Encoded protein function: FUNCTION: May be involved in the biogenesis of curli organelles. EcoCyc product frame: G6544-MONOMER. Genomic coordinates: 1101711-1102127. EcoCyc protein note: The curli specific genes are present in two divergently transcribed operons, csgDEFG and csgBAC, which encode the structural, accessory and regulatory proteins of the curli biosynthetic pathway (reviewed in ). CsgF localizes to the outer membrane where it interacts with CsgG to form the curli secretion channel complex; CsgF also interacts with the the curli nucleator protein G6547-MONOMER "CsgB" to promote curli subunit polymerisation. A polar mutation in csgF (csgF1::Tn104) abolishes curli formation . CsgF is localized on the outer surface of the outer membrane; in the absence of CsgF, both CsgB and EG11489-MONOMER "CsgA" are secreted away from the cell; CsgF has a role in CsgB nucleator function . CsgF and CsgG physically interact at the outer membrane . CsgF interacts with CsgB and accelerates self assembly of CsgB into an amyloid-templating conformation in vitro . CsgG and CsgF from a stable complex with a 9:9 stoichiometric ratio...

## Biological Role

Repressed by rybB (gene.b4417), mcaS (gene.b4426), rprA (gene.b4431), omrA (gene.b4444), omrB (gene.b4445), hns (protein.P0ACF8), cpxR (protein.P0AE88), btsR (protein.P0AFT5), and 3 more. Activated by rpoD (protein.P00579), ompR (protein.P0AA16), cra (protein.P0ACP1), rpoS (protein.P13445), basR (protein.P30843), mlrA (protein.P33358), csgD (protein.P52106), rcdA (protein.P75811).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AE98|protein.P0AE98]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (19)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=csgF; function=+
- `activates` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `C` - regulator=OmpR; target=csgF; function=+
- `activates` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=csgF; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=csgF; function=+
- `activates` <-- [[protein.P30843|protein.P30843]] `RegulonDB` `S` - regulator=BasR; target=csgF; function=+
- `activates` <-- [[protein.P33358|protein.P33358]] `RegulonDB` `S` - regulator=MlrA; target=csgF; function=+
- `activates` <-- [[protein.P52106|protein.P52106]] `RegulonDB` `S` - regulator=CsgD; target=csgF; function=+
- `activates` <-- [[protein.P75811|protein.P75811]] `RegulonDB` `S` - regulator=RcdA; target=csgF; function=+
- `represses` <-- [[gene.b4417|gene.b4417]] `RegulonDB` `S` - regulator=RybB; target=csgF; function=-
- `represses` <-- [[gene.b4426|gene.b4426]] `RegulonDB` `S` - regulator=McaS; target=csgF; function=-
- `represses` <-- [[gene.b4431|gene.b4431]] `RegulonDB` `S` - regulator=RprA; target=csgF; function=-
- `represses` <-- [[gene.b4444|gene.b4444]] `RegulonDB` `S` - regulator=OmrA; target=csgF; function=-
- `represses` <-- [[gene.b4445|gene.b4445]] `RegulonDB` `S` - regulator=OmrB; target=csgF; function=-
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=csgF; function=-
- `represses` <-- [[protein.P0AE88|protein.P0AE88]] `RegulonDB` `S` - regulator=CpxR; target=csgF; function=-
- `represses` <-- [[protein.P0AFT5|protein.P0AFT5]] `RegulonDB` `S` - regulator=BtsR; target=csgF; function=-
- `represses` <-- [[protein.P52108|protein.P52108]] `RegulonDB` `S` - regulator=RstA; target=csgF; function=-
- `represses` <-- [[protein.P52627|protein.P52627]] `RegulonDB` `S` - regulator=FliZ; target=csgF; function=-
- `represses` <-- [[protein.Q46864|protein.Q46864]] `RegulonDB` `S` - regulator=MqsA; target=csgF; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003519,ECOCYC:G6544,GeneID:945622`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1101711-1102127:-; feature_type=gene
