---
entity_id: "protein.Q47319"
entity_type: "protein"
name: "tapT"
source_database: "UniProt"
source_id: "Q47319"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tapT tuaA yfiP b2583 JW5409"
---

# tapT

`protein.Q47319`

## Static

- Type: `protein`
- Source: `UniProt:Q47319`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the formation of 3-(3-amino-3-carboxypropyl)uridine (acp3U) at position 47 of tRNAs (PubMed:31804502, PubMed:31863583, PubMed:4597321). Acp3U47 confers thermal stability on tRNA (PubMed:31804502). {ECO:0000269|PubMed:31804502, ECO:0000269|PubMed:31863583, ECO:0000269|PubMed:4597321}. tRNA-uridine aminocarboxypropyltransferase catalyzes the transfer of the aminocarboxypropyl group from S-adenosylmethionine to the N3 position of uridine within tRNAs . The physiological significance of the 3-(3-amino-3-carboxypropyl)uridine (acp3U) modification is so far unknown . The acp3U modification of tRNAs is widely conserved ; in E. coli, it resides in nucleotide 47 of the variable loop of eight specific tRNAs and appears to increase their thermal stability . Depending on the specific tRNA, lack of prior m7G modification at position 46 reduces acp3U modification . A structural model of TapT suggests the presence of a trefoil knot that is characteristic of the α/β knot methyltransferase superfamily . TapT binds Zn2+ in vitro; the N-terminal domain of TapT with a putative zinc-binding motif is required for catalytic activity. Mutations in the conserved DTW motif strongly reduce activity . A ΔtapT mutant has no obvious defect under normal growth conditions ; when cultured under continuous heat stress, it develops a motility defect due to secondary mutations...

## Biological Role

Catalyzes RXN-21179 (reaction.ecocyc.RXN-21179).

## Annotation

FUNCTION: Catalyzes the formation of 3-(3-amino-3-carboxypropyl)uridine (acp3U) at position 47 of tRNAs (PubMed:31804502, PubMed:31863583, PubMed:4597321). Acp3U47 confers thermal stability on tRNA (PubMed:31804502). {ECO:0000269|PubMed:31804502, ECO:0000269|PubMed:31863583, ECO:0000269|PubMed:4597321}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-21179|reaction.ecocyc.RXN-21179]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2583|gene.b2583]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q47319`
- `KEGG:ecj:JW5409;eco:b2583;ecoc:C3026_14315;`
- `GeneID:947057;`
- `GO:GO:0006400; GO:0008270; GO:0016432`
- `EC:2.5.1.25`

## Notes

tRNA-uridine aminocarboxypropyltransferase (EC 2.5.1.25) (SAM-dependent 3-amino-3-carboxypropyl transferase) (tRNA U47 acp transferase A) (tRNA aminocarboxypropyltransferase)
