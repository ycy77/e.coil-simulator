---
entity_id: "protein.P21369"
entity_type: "protein"
name: "pncA"
source_database: "UniProt"
source_id: "P21369"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pncA nam ydjB b1768 JW1757"
---

# pncA

`protein.P21369`

## Static

- Type: `protein`
- Source: `UniProt:P21369`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the deamidation of nicotinamide (NAM) into nicotinate (PubMed:4399474, PubMed:8726014). Likely functions in the cyclical salvage pathway for production of NAD from nicotinamide (PubMed:4399474). {ECO:0000269|PubMed:4399474, ECO:0000305|PubMed:8726014}.; FUNCTION: Is also able to hydrolyze the first-line antituberculous drug pyrazinamide (PZA) into pyrazinoic acid in vitro, but this reaction is not considered to be physiologically relevant. {ECO:0000305|PubMed:8726014}. pncA encodes a nicotinamidase (a member of the isochorismatase superfamily) that is active in the cyclical salvage pathway for production of NAD+ from nicotinamide (see pathway PYRIDNUCSAL-PWY). Homologs of PncA are found in other bacteria, archaea, and some eukaryotes, but not in vertebrates (reviewed in ). Early work established this salvage pathway in E. coli and a role for nicotinamidase . Exogenous nicotinamide appears to be passively taken up by E. coli . The pncA-encoded nicotinamidase also has pyrazinamidase activity. PYRAZINAMIDE Pyrazinamide is an antibiotic with a structure similar to nicotinamide ; it is an antituberculosis prodrug that is hydrolytically converted to its active form, pyrazine-2-carboxylate (pyrazinoic acid), by the pyrazinamidase activity of PncA. However, this drug is not a relevant antibiotic for E. coli, which is naturally resistant...

## Biological Role

Catalyzes NICOTINAMID-RXN (reaction.ecocyc.NICOTINAMID-RXN), PYRAZIN-RXN (reaction.ecocyc.PYRAZIN-RXN). Bound by Zinc cation (molecule.C00038).

## Enriched Pathways

- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the deamidation of nicotinamide (NAM) into nicotinate (PubMed:4399474, PubMed:8726014). Likely functions in the cyclical salvage pathway for production of NAD from nicotinamide (PubMed:4399474). {ECO:0000269|PubMed:4399474, ECO:0000305|PubMed:8726014}.; FUNCTION: Is also able to hydrolyze the first-line antituberculous drug pyrazinamide (PZA) into pyrazinoic acid in vitro, but this reaction is not considered to be physiologically relevant. {ECO:0000305|PubMed:8726014}.

## Pathways

- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.NICOTINAMID-RXN|reaction.ecocyc.NICOTINAMID-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.PYRAZIN-RXN|reaction.ecocyc.PYRAZIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b1768|gene.b1768]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P21369`
- `KEGG:ecj:JW1757;eco:b1768;ecoc:C3026_10095;`
- `GeneID:946276;`
- `GO:GO:0005829; GO:0008936; GO:0016811; GO:0019365; GO:0046872`
- `EC:3.5.1.-; 3.5.1.19`

## Notes

Nicotinamidase (EC 3.5.1.19) (Nicotinamide deamidase) (NAMase) (Pyrazinamidase) (PZAase) (EC 3.5.1.-)
