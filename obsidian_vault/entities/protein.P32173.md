---
entity_id: "protein.P32173"
entity_type: "protein"
name: "mobA"
source_database: "UniProt"
source_id: "P32173"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mobA chlB mob narB b3857 JW3829"
---

# mobA

`protein.P32173`

## Static

- Type: `protein`
- Source: `UniProt:P32173`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Transfers a GMP moiety from GTP to Mo-molybdopterin (Mo-MPT) cofactor (Moco or molybdenum cofactor) to form Mo-molybdopterin guanine dinucleotide (Mo-MGD) cofactor. Is also involved in the biosynthesis of the bis-MGD form of the Moco cofactor (Mo-bisMGD) in which the metal is symmetrically ligated by the dithiolene groups of two MGD molecules. Is necessary and sufficient for the in vitro activation of the DMSOR molybdoenzyme that uses the Mo-bisMGD form of molybdenum cofactor, which implies formation and efficient insertion of the cofactor into the enzyme without the need of a chaperone. Is specific for GTP since other nucleotides such as ATP and GMP cannot be utilized. {ECO:0000269|PubMed:10978348, ECO:0000269|PubMed:1648082, ECO:0000269|PubMed:21081498, ECO:0000269|PubMed:8020507}. MobA is required for the biosynthesis of the molybdopterin guanine dinucleotide (MGD) cofactor . The enzyme catalyzes the transfer of a GMP moiety from GTP to Mo-molybdopterin, forming MGD . The MGD cofactor can be further modified to CPD-15873 "bis-MGD". Formation of bis-MGD is proposed to involve formation of a CPD-15874 "bis-Mo-MPT" intermediate followed by the addition of two GMP moieties by MobA. This cofactor is then transferred to its target protein TorA . MobA is monomeric in solution . Crystal structures of MobA have been solved...

## Biological Role

Catalyzes RXN-21601 (reaction.ecocyc.RXN-21601), RXN0-262 (reaction.ecocyc.RXN0-262). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Transfers a GMP moiety from GTP to Mo-molybdopterin (Mo-MPT) cofactor (Moco or molybdenum cofactor) to form Mo-molybdopterin guanine dinucleotide (Mo-MGD) cofactor. Is also involved in the biosynthesis of the bis-MGD form of the Moco cofactor (Mo-bisMGD) in which the metal is symmetrically ligated by the dithiolene groups of two MGD molecules. Is necessary and sufficient for the in vitro activation of the DMSOR molybdoenzyme that uses the Mo-bisMGD form of molybdenum cofactor, which implies formation and efficient insertion of the cofactor into the enzyme without the need of a chaperone. Is specific for GTP since other nucleotides such as ATP and GMP cannot be utilized. {ECO:0000269|PubMed:10978348, ECO:0000269|PubMed:1648082, ECO:0000269|PubMed:21081498, ECO:0000269|PubMed:8020507}.

## Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-21601|reaction.ecocyc.RXN-21601]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-262|reaction.ecocyc.RXN0-262]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3857|gene.b3857]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P32173`
- `KEGG:ecj:JW3829;eco:b3857;ecoc:C3026_20850;`
- `GeneID:948349;`
- `GO:GO:0000287; GO:0005525; GO:0005737; GO:0016779; GO:0061603; GO:1902758`
- `EC:2.7.7.77`

## Notes

Molybdenum cofactor guanylyltransferase (MoCo guanylyltransferase) (EC 2.7.7.77) (GTP:molybdopterin guanylyltransferase) (Mo-MPT guanylyltransferase) (Molybdopterin guanylyltransferase) (Molybdopterin-guanine dinucleotide biosynthesis protein A) (Molybdopterin-guanine dinucleotide synthase) (MGD synthase) (Protein FA)
