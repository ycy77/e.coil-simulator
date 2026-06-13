---
entity_id: "gene.b1037"
entity_type: "gene"
name: "csgG"
source_database: "NCBI RefSeq"
source_id: "gene-b1037"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1037"
  - "csgG"
---

# csgG

`gene.b1037`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1037`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

csgG (gene.b1037) is a gene entity. It encodes csgG (protein.P0AEA2). Encoded protein function: FUNCTION: May be involved in the biogenesis of curli organelles. EcoCyc product frame: G6543-MONOMER. Genomic coordinates: 1100851-1101684. EcoCyc protein note: CsgG is an outer membrane lipoprotein which forms the secretion channel for curli subunits. A transposon insertion in csgG abolishes curli production without affecting production of the EG11489-MONOMER "CsgA" curlin subunit . CsgG is a periplasmic facing outer membrane lipoprotein which folds into a protease-resistant conformation . Purified CsgG forms pore containing oligomers; CsgG interacts with G6545-MONOMER "CsgE" and G6544-MONOMER "CsgF" at the outer membrane | (see further ). CsgG clusters into foci in curli-producing cells . CsgG forms a nonameric transmembrane channel in the outer membrane with a large solvent accessible periplasmic cavity; the cavity is open to the periplasm but is constricted to form a pore at the membrane interface; the size of the pore eyelet suggests that curli subunits are secreted in unfolded form; three aromatic residues (Phe63, Tyr66 and Phe71) located at the pore eyelet may have a role in recognising curli subunits (see further ). Overexpression of CsgG increases sensitivity to the hydrophobic antibiotic, erythromycin...

## Biological Role

Repressed by rybB (gene.b4417), mcaS (gene.b4426), rprA (gene.b4431), omrA (gene.b4444), omrB (gene.b4445), hns (protein.P0ACF8), cpxR (protein.P0AE88), btsR (protein.P0AFT5), and 3 more. Activated by rpoD (protein.P00579), ompR (protein.P0AA16), cra (protein.P0ACP1), rpoS (protein.P13445), basR (protein.P30843), mlrA (protein.P33358), csgD (protein.P52106), rcdA (protein.P75811).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEA2|protein.P0AEA2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (19)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=csgG; function=+
- `activates` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `C` - regulator=OmpR; target=csgG; function=+
- `activates` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `C` - regulator=Cra; target=csgG; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=csgG; function=+
- `activates` <-- [[protein.P30843|protein.P30843]] `RegulonDB` `S` - regulator=BasR; target=csgG; function=+
- `activates` <-- [[protein.P33358|protein.P33358]] `RegulonDB` `S` - regulator=MlrA; target=csgG; function=+
- `activates` <-- [[protein.P52106|protein.P52106]] `RegulonDB` `S` - regulator=CsgD; target=csgG; function=+
- `activates` <-- [[protein.P75811|protein.P75811]] `RegulonDB` `S` - regulator=RcdA; target=csgG; function=+
- `represses` <-- [[gene.b4417|gene.b4417]] `RegulonDB` `S` - regulator=RybB; target=csgG; function=-
- `represses` <-- [[gene.b4426|gene.b4426]] `RegulonDB` `S` - regulator=McaS; target=csgG; function=-
- `represses` <-- [[gene.b4431|gene.b4431]] `RegulonDB` `S` - regulator=RprA; target=csgG; function=-
- `represses` <-- [[gene.b4444|gene.b4444]] `RegulonDB` `S` - regulator=OmrA; target=csgG; function=-
- `represses` <-- [[gene.b4445|gene.b4445]] `RegulonDB` `S` - regulator=OmrB; target=csgG; function=-
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=csgG; function=-
- `represses` <-- [[protein.P0AE88|protein.P0AE88]] `RegulonDB` `S` - regulator=CpxR; target=csgG; function=-
- `represses` <-- [[protein.P0AFT5|protein.P0AFT5]] `RegulonDB` `S` - regulator=BtsR; target=csgG; function=-
- `represses` <-- [[protein.P52108|protein.P52108]] `RegulonDB` `S` - regulator=RstA; target=csgG; function=-
- `represses` <-- [[protein.P52627|protein.P52627]] `RegulonDB` `S` - regulator=FliZ; target=csgG; function=-
- `represses` <-- [[protein.Q46864|protein.Q46864]] `RegulonDB` `S` - regulator=MqsA; target=csgG; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003516,ECOCYC:G6543,GeneID:945619`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1100851-1101684:-; feature_type=gene
