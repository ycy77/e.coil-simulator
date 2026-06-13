---
entity_id: "gene.b1039"
entity_type: "gene"
name: "csgE"
source_database: "NCBI RefSeq"
source_id: "gene-b1039"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1039"
  - "csgE"
---

# csgE

`gene.b1039`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1039`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

csgE (gene.b1039) is a gene entity. It encodes csgE (protein.P0AE95). Encoded protein function: FUNCTION: May be involved in the biogenesis of curli organelles. EcoCyc product frame: G6545-MONOMER. Genomic coordinates: 1102152-1102541. EcoCyc protein note: The curli specific genes are present in two divergently transcribed operons, csgDEFG and csgBAC, which encode the structural, accessory and regulatory proteins of the curli biosynthetic pathway (reviewed in ). G6545-MONOMER "CsgE" forms a nonameric structure which binds to the periplasmic face of the CsgGF outer membrane CPLX-3945 ; CsgE also binds to the major curlin subunit EG11489-MONOMER "CsgA" and it is proposed that CsgE may act to capture and confine CsgA into the secretion complex for outward translocation (see also ). A transposon insertion in csgE abolishes curli production without affecting production of the EG11489-MONOMER "CsgA" curlin subunit . Deletion of csgE results in a significant decrease in the level of detectable CsgA, CsgF and CsgB . CsgE interacts with CsgG and CsgF at the outer membrane . CsgE is able to restrict CsgG dependent secretion of non-curli substrates but does not restrict secretion of substrates with a putative curli secretion signal . CsgE reverses the erythromycin sensitive phenotype of csgG overexpression . CsgE prevents the self-assembly of soluble CsgA into amyloid fibres in vitro...

## Biological Role

Repressed by rybB (gene.b4417), mcaS (gene.b4426), rprA (gene.b4431), omrA (gene.b4444), omrB (gene.b4445), hns (protein.P0ACF8), cpxR (protein.P0AE88), btsR (protein.P0AFT5), and 3 more. Activated by rpoD (protein.P00579), ompR (protein.P0AA16), cra (protein.P0ACP1), rpoS (protein.P13445), basR (protein.P30843), mlrA (protein.P33358), csgD (protein.P52106), rcdA (protein.P75811).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AE95|protein.P0AE95]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (19)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=csgE; function=+
- `activates` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `C` - regulator=OmpR; target=csgE; function=+
- `activates` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=csgE; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=csgE; function=+
- `activates` <-- [[protein.P30843|protein.P30843]] `RegulonDB` `S` - regulator=BasR; target=csgE; function=+
- `activates` <-- [[protein.P33358|protein.P33358]] `RegulonDB` `S` - regulator=MlrA; target=csgE; function=+
- `activates` <-- [[protein.P52106|protein.P52106]] `RegulonDB` `S` - regulator=CsgD; target=csgE; function=+
- `activates` <-- [[protein.P75811|protein.P75811]] `RegulonDB` `S` - regulator=RcdA; target=csgE; function=+
- `represses` <-- [[gene.b4417|gene.b4417]] `RegulonDB` `S` - regulator=RybB; target=csgE; function=-
- `represses` <-- [[gene.b4426|gene.b4426]] `RegulonDB` `S` - regulator=McaS; target=csgE; function=-
- `represses` <-- [[gene.b4431|gene.b4431]] `RegulonDB` `S` - regulator=RprA; target=csgE; function=-
- `represses` <-- [[gene.b4444|gene.b4444]] `RegulonDB` `S` - regulator=OmrA; target=csgE; function=-
- `represses` <-- [[gene.b4445|gene.b4445]] `RegulonDB` `S` - regulator=OmrB; target=csgE; function=-
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=csgE; function=-
- `represses` <-- [[protein.P0AE88|protein.P0AE88]] `RegulonDB` `S` - regulator=CpxR; target=csgE; function=-
- `represses` <-- [[protein.P0AFT5|protein.P0AFT5]] `RegulonDB` `S` - regulator=BtsR; target=csgE; function=-
- `represses` <-- [[protein.P52108|protein.P52108]] `RegulonDB` `S` - regulator=RstA; target=csgE; function=-
- `represses` <-- [[protein.P52627|protein.P52627]] `RegulonDB` `S` - regulator=FliZ; target=csgE; function=-
- `represses` <-- [[protein.Q46864|protein.Q46864]] `RegulonDB` `S` - regulator=MqsA; target=csgE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003528,ECOCYC:G6545,GeneID:945711`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1102152-1102541:-; feature_type=gene
