---
entity_id: "protein.P0AET8"
entity_type: "protein"
name: "hdhA"
source_database: "UniProt"
source_id: "P0AET8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hdhA hsdH b1619 JW1611"
---

# hdhA

`protein.P0AET8`

## Static

- Type: `protein`
- Source: `UniProt:P0AET8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: 7alpha-hydroxysteroid dehydrogenase involved in the metabolism of bile acids. Catalyzes the NAD(+)-dependent oxidation of the 7alpha-hydroxy group of 7alpha-hydroxysteroids, such as the major human bile acids cholate and chenodeoxycholate, to the corresponding 7-oxosteroids. To a lesser extent, can also act on taurochenodeoxycholate, taurocholate and glycocholate (PubMed:2007545). Can also use glycochenodeoxycholate as substrate (PubMed:8672472). Is not able to use NADP(+) instead of NAD(+) as the electron acceptor (PubMed:2007545). {ECO:0000269|PubMed:2007545, ECO:0000269|PubMed:8672472}. 7-α-hydroxysteroid dehydrogenase catalyzes the dehydroxylation of cholic and chenodeoxycholic acids, major human bile acids, yielding 7-oxocholic and 7-oxochenodeoxycholic acids, respectively. The enzyme belongs to the short-chain nonmetalloenzyme-alcohol dehydrogenase protein family. The enzyme shows activity with several substrates having a hydroxyl group at position 7 of the steroid skeleton. NAD+ is required for enzyme activity . Crystal structures of the enzyme in binary and ternary complexes have been solved. Substrate binding induces a large conformational change at the substrate binding loop and in the C-terminal amino acids. A catalytic mechanism has been proposed . Site-directed mutagenesis of proposed catalytic residues confirmed their roles...

## Biological Role

Catalyzes 3alpha,7alpha,12alpha-trihydroxy-5beta-cholanate:NAD+ 7-oxidoreductase (reaction.R02792). Component of 7-α-hydroxysteroid dehydrogenase (complex.ecocyc.7-ALPHA-HYDROXYSTEROID-DEH-CPLX).

## Enriched Pathways

- `eco00121` Secondary bile acid biosynthesis (KEGG)

## Annotation

FUNCTION: 7alpha-hydroxysteroid dehydrogenase involved in the metabolism of bile acids. Catalyzes the NAD(+)-dependent oxidation of the 7alpha-hydroxy group of 7alpha-hydroxysteroids, such as the major human bile acids cholate and chenodeoxycholate, to the corresponding 7-oxosteroids. To a lesser extent, can also act on taurochenodeoxycholate, taurocholate and glycocholate (PubMed:2007545). Can also use glycochenodeoxycholate as substrate (PubMed:8672472). Is not able to use NADP(+) instead of NAD(+) as the electron acceptor (PubMed:2007545). {ECO:0000269|PubMed:2007545, ECO:0000269|PubMed:8672472}.

## Pathways

- `eco00121` Secondary bile acid biosynthesis (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R02792|reaction.R02792]] `KEGG` `database` - via EC:1.1.1.159
- `is_component_of` --> [[complex.ecocyc.7-ALPHA-HYDROXYSTEROID-DEH-CPLX|complex.ecocyc.7-ALPHA-HYDROXYSTEROID-DEH-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b1619|gene.b1619]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AET8`
- `KEGG:ag:BAA01384;ecj:JW1611;eco:b1619;ecoc:C3026_09310;`
- `GeneID:75171679;946151;`
- `GO:GO:0005829; GO:0008709; GO:0016042; GO:0030573; GO:0032991; GO:0042802; GO:0051287; GO:0106281`
- `EC:1.1.1.159`

## Notes

7alpha-hydroxysteroid dehydrogenase (7alpha-HSDH) (EC 1.1.1.159) (NAD-dependent 7alpha-hydroxysteroid dehydrogenase)
