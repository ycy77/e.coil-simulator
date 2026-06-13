---
entity_id: "protein.P37661"
entity_type: "protein"
name: "eptB"
source_database: "UniProt"
source_id: "P37661"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15795227}; Multi-pass membrane protein {ECO:0000269|PubMed:15795227}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "eptB yhjW b3546 JW5660"
---

# eptB

`protein.P37661`

## Static

- Type: `protein`
- Source: `UniProt:P37661`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15795227}; Multi-pass membrane protein {ECO:0000269|PubMed:15795227}.

## Enriched Summary

FUNCTION: Catalyzes the addition of a phosphoethanolamine (pEtN) moiety to the outer 3-deoxy-D-manno-octulosonic acid (Kdo) residue of a Kdo(2)-lipid A. Phosphatidylethanolamines with one unsaturated acyl group function as pEtN donors and the reaction releases diacylglycerol. {ECO:0000269|PubMed:15795227}. EptB catalyses the addition of phosphoethanolamine (pEtN) to the 3-deoxy-d-manno-oct-2-ulosonate (KdoII) sugar of the inner core of lipid A-core oligosaccharide. Lipopolysaccharide, isolated from an E. coli K-12 W3110 derived A-DEEP-ROUGH-FORM-LIPOPOLYSACCHARIDE deep rough (Re) mutant (E. coli WBB06) contains non-stoichiometric pEtN substitutions at position 7 of the second Kdo residue . Addition of the pEtN moiety to the Kdo region of Re LPS is absolutely dependent upon the presence of CaCl2 in the growth medium; LPS isolated from strain WBB06 grown in rich media does not contain detectable pEtN substitutents; membrane preparations from wild-type W3110 and mutant WBB06 grown in the presence of 5-50 mm CaCl2 both contain an enzyme activity that modifies the outer Kdo sugar of the LPS core with a pEtN moiety; calcium-induced pEtN transferase activity is not seen in membranes of an E. coli EG10781 pssA null mutant suggesting that phosphatidylethanolamine is the donor substrate for the pEtN moiety...

## Biological Role

Catalyzes RXN-16286 (reaction.ecocyc.RXN-16286), RXN-22561 (reaction.ecocyc.RXN-22561), RXN0-4581 (reaction.ecocyc.RXN0-4581).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Annotation

FUNCTION: Catalyzes the addition of a phosphoethanolamine (pEtN) moiety to the outer 3-deoxy-D-manno-octulosonic acid (Kdo) residue of a Kdo(2)-lipid A. Phosphatidylethanolamines with one unsaturated acyl group function as pEtN donors and the reaction releases diacylglycerol. {ECO:0000269|PubMed:15795227}.

## Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.RXN-16286|reaction.ecocyc.RXN-16286]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-22561|reaction.ecocyc.RXN-22561]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-4581|reaction.ecocyc.RXN0-4581]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3546|gene.b3546]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37661`
- `KEGG:ecj:JW5660;eco:b3546;ecoc:C3026_19225;`
- `GeneID:948068;`
- `GO:GO:0005886; GO:0009244; GO:0009245; GO:0043838`
- `EC:2.7.8.42`

## Notes

Kdo(2)-lipid A phosphoethanolamine 7''-transferase (EC 2.7.8.42) (Phosphoethanolamine transferase EptB)
