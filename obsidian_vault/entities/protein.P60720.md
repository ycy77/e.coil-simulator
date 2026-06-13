---
entity_id: "protein.P60720"
entity_type: "protein"
name: "lipB"
source_database: "UniProt"
source_id: "P60720"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00013}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lipB b0630 JW5089"
---

# lipB

`protein.P60720`

## Static

- Type: `protein`
- Source: `UniProt:P60720`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00013}.

## Enriched Summary

FUNCTION: Catalyzes the transfer of endogenously produced octanoic acid from octanoyl-acyl-carrier-protein onto the lipoyl domains of lipoate-dependent enzymes. Lipoyl-ACP can also act as a substrate although octanoyl-ACP is likely to be the physiological substrate. {ECO:0000255|HAMAP-Rule:MF_00013, ECO:0000269|PubMed:15642479, ECO:0000269|PubMed:16342964}. LipB is a lipoyl-/octanoyl-ACP:protein transferase that catalyzes the first step of de novo lipoate biosynthesis . In vitro, it transfers lipoyl or octanoyl domains from the corresponding acylated ACP to its target proteins; in vivo, octanoyl-ACP is the relevant substrate. Lipoate modification of the E2 subunits is important for the function of PYRUVATEDEH-CPLX , 2OXOGLUTARATEDEH-CPLX "α-ketoglutarate dehydrogenase" , and the GCVMULTI-CPLX . The LipB protein is translated from a TTG translation initiation codon ; protein translated from the downstream ATG is not active . The LipB-catalyzed reaction proceeds via an acyl-enzyme intermediate. The octanoate group is first transferred from the thiol of ACP to the C169 thiol of LipB, followed by transfer to a specific lysine residue of E2 subunits . Allosteric regulation controls this transfer of the octanoic acid...

## Biological Role

Catalyzes octanoyl-[acp]:protein N6-octanoyltransferase (reaction.R07766), lipoyl-[acp]:protein N6-lipoyltransferase (reaction.R07769), RXN0-1130 (reaction.ecocyc.RXN0-1130), RXN0-1137 (reaction.ecocyc.RXN0-1137), RXN0-1138 (reaction.ecocyc.RXN0-1138), RXN0-947 (reaction.ecocyc.RXN0-947).

## Enriched Pathways

- `eco00785` Lipoic acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the transfer of endogenously produced octanoic acid from octanoyl-acyl-carrier-protein onto the lipoyl domains of lipoate-dependent enzymes. Lipoyl-ACP can also act as a substrate although octanoyl-ACP is likely to be the physiological substrate. {ECO:0000255|HAMAP-Rule:MF_00013, ECO:0000269|PubMed:15642479, ECO:0000269|PubMed:16342964}.

## Pathways

- `eco00785` Lipoic acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (6)

- `catalyzes` --> [[reaction.R07766|reaction.R07766]] `KEGG` `database` - via EC:2.3.1.181
- `catalyzes` --> [[reaction.R07769|reaction.R07769]] `KEGG` `database` - via EC:2.3.1.181
- `catalyzes` --> [[reaction.ecocyc.RXN0-1130|reaction.ecocyc.RXN0-1130]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-1137|reaction.ecocyc.RXN0-1137]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-1138|reaction.ecocyc.RXN0-1138]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-947|reaction.ecocyc.RXN0-947]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0630|gene.b0630]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P60720`
- `KEGG:ecj:JW5089;eco:b0630;ecoc:C3026_03150;`
- `GeneID:93776852;945217;`
- `GO:GO:0003824; GO:0005737; GO:0009106; GO:0009107; GO:0009249; GO:0010629; GO:0016740; GO:0033819`
- `EC:2.3.1.181`

## Notes

Octanoyltransferase (EC 2.3.1.181) (Lipoate-protein ligase B) (Lipoyl/octanoyl transferase) (Octanoyl-[acyl-carrier-protein]-protein N-octanoyltransferase)
