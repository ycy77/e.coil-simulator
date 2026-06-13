---
entity_id: "protein.P33225"
entity_type: "protein"
name: "torA"
source_database: "UniProt"
source_id: "P33225"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:2512991}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "torA b0997 JW0982"
---

# torA

`protein.P33225`

## Static

- Type: `protein`
- Source: `UniProt:P33225`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:2512991}.

## Enriched Summary

FUNCTION: Reduces trimethylamine-N-oxide (TMAO) into trimethylamine; an anaerobic reaction coupled to energy-yielding reactions. {ECO:0000269|PubMed:30945846, ECO:0000269|PubMed:39769096}. torA encodes an inducible trimethylamine N-oxide reductase. The enzyme functions as a terminal reductase during anaerobic respiration on TMAO - early work was done using E. coli K-10 . TorA contains the site of TMAO reduction and the CPD-15873 . The presence of the GMP nucleotides is crucial for the insertion of the cofactor into the apo enzyme . Purified TorA cannot reduce sulfoxides (including dimethylsulfoxide - DMSO) and has high specificity for the two N-oxides - TMAO and 4 methylmorpholine-N-oxide . There is some evidence that TorA can exist as both a dimer and a monomer . A 39 amino acid signal peptide is cleaved . Tor A receives electrons from the membrane bound cytochrome c menaquinol dehydrogenase TorC EG12195-MONOMER "TorD" is the dedicated chaperone of TorA; TorD is involved in the protection and maturation of TorA . torC, torA and torD form an operon which is regulated by the PWY0-1506 "TorTSR two component system" . Expression is induced by trimethylamine N-oxide (TMAO) and repressed by oxygen; expression is not directly regulated by EG10325 "Fnr" . The sulfoxides DMSO and TMSO (tetramethylenesulfoxide) induce expression of torCA but are not substrates of the enzyme...

## Biological Role

Catalyzes RXN-19618 (reaction.ecocyc.RXN-19618). Component of menaquinol:trimethylamine N-oxide oxidoreductase I (complex.ecocyc.TMAOREDUCTI-CPLX). Bound by bis(guanylyl molybdopterin) cofactor (molecule.ecocyc.CPD-15873).

## Enriched Pathways

- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Reduces trimethylamine-N-oxide (TMAO) into trimethylamine; an anaerobic reaction coupled to energy-yielding reactions. {ECO:0000269|PubMed:30945846, ECO:0000269|PubMed:39769096}.

## Pathways

- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-19618|reaction.ecocyc.RXN-19618]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.TMAOREDUCTI-CPLX|complex.ecocyc.TMAOREDUCTI-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.CPD-15873|molecule.ecocyc.CPD-15873]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0997|gene.b0997]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33225`
- `KEGG:ecj:JW0982;eco:b0997;ecoc:C3026_06075;`
- `GeneID:946267;`
- `GO:GO:0006885; GO:0009055; GO:0009060; GO:0009061; GO:0019645; GO:0030151; GO:0030288; GO:0043546; GO:0050626; GO:1904852`
- `EC:1.7.2.3`

## Notes

Trimethylamine-N-oxide reductase 1 (TMAO reductase 1) (Trimethylamine oxidase 1) (EC 1.7.2.3)
