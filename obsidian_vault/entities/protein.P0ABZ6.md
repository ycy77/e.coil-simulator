---
entity_id: "protein.P0ABZ6"
entity_type: "protein"
name: "surA"
source_database: "UniProt"
source_id: "P0ABZ6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm. Note=Is capable of associating with the outer membrane."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "surA b0053 JW0052"
---

# surA

`protein.P0ABZ6`

## Static

- Type: `protein`
- Source: `UniProt:P0ABZ6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm. Note=Is capable of associating with the outer membrane.

## Enriched Summary

FUNCTION: Chaperone involved in the correct folding and assembly of outer membrane proteins, such as OmpA, OmpF and LamB (PubMed:8985185). Recognizes specific patterns of aromatic residues and the orientation of their side chains, which are found more frequently in integral outer membrane proteins (PubMed:8985185). May act in both early periplasmic and late outer membrane-associated steps of protein maturation (PubMed:2165476). Essential for the survival of E.coli in stationary phase. Required for pilus biogenesis (PubMed:16267292). {ECO:0000269|PubMed:16267292, ECO:0000269|PubMed:2165476, ECO:0000269|PubMed:8985185}. SurA is a periplasmic chaperone involved in the biogenesis of outer membrane proteins (OMPs). SurA is required for proper assembly of the outer membrane proteins EG10669-MONOMER OmpA, CPLX0-7534 OmpF, and CPLX0-7655 LamB ; loss of SurA is associated with a defective outer membrane and induction of RPOE-MONOMER "σE" activity; surA null mutants show increased sensitivity to detergents, bile salts and some antibiotics (see further ). Depletion of SurA reduces the density of the outer membrane . The purified protein has (low) peptidyl-prolyl isomerase (PPI) activity on model substrates . SurA is required for growth at pH 9 . Combining null mutations in G7320 "bamB" and surA is synthetically lethal...

## Biological Role

Catalyzes PEPTIDYLPROLYL-ISOMERASE-RXN (reaction.ecocyc.PEPTIDYLPROLYL-ISOMERASE-RXN).

## Annotation

FUNCTION: Chaperone involved in the correct folding and assembly of outer membrane proteins, such as OmpA, OmpF and LamB (PubMed:8985185). Recognizes specific patterns of aromatic residues and the orientation of their side chains, which are found more frequently in integral outer membrane proteins (PubMed:8985185). May act in both early periplasmic and late outer membrane-associated steps of protein maturation (PubMed:2165476). Essential for the survival of E.coli in stationary phase. Required for pilus biogenesis (PubMed:16267292). {ECO:0000269|PubMed:16267292, ECO:0000269|PubMed:2165476, ECO:0000269|PubMed:8985185}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.PEPTIDYLPROLYL-ISOMERASE-RXN|reaction.ecocyc.PEPTIDYLPROLYL-ISOMERASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0053|gene.b0053]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABZ6`
- `KEGG:ecj:JW0052;eco:b0053;ecoc:C3026_00275;`
- `GeneID:93777382;944812;`
- `GO:GO:0003755; GO:0006457; GO:0030288; GO:0036506; GO:0042277; GO:0043165; GO:0050821; GO:0051082`
- `EC:5.2.1.8`

## Notes

Chaperone SurA (Peptidyl-prolyl cis-trans isomerase SurA) (PPIase SurA) (EC 5.2.1.8) (Rotamase SurA) (Survival protein A)
