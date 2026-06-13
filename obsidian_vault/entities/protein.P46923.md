---
entity_id: "protein.P46923"
entity_type: "protein"
name: "torZ"
source_database: "UniProt"
source_id: "P46923"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:11004177}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "torZ bisZ b1872 JW1861"
---

# torZ

`protein.P46923`

## Static

- Type: `protein`
- Source: `UniProt:P46923`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:11004177}.

## Enriched Summary

FUNCTION: Reduces trimethylamine-N-oxide (TMAO) into trimethylamine; an anaerobic reaction coupled to energy-yielding reactions. Can also reduce other N- and S-oxide compounds such as 4-methylmorpholine-N-oxide and biotin sulfoxide (BSO), but with a lower catalytic efficiency. {ECO:0000269|PubMed:11004177}. The periplasmic oxidoreductase TorZ and pentaheme c-type cytochrome G7023-MONOMER "TorY" constitute an anaerobic respiratory system that can use several N and S-oxides, including trimethylamine n--oxide (TMAO) and biotin sulfoxide (BSO) as terminal electron acceptors . TorZ (formerly BisZ) is responsible for the small amount of biotin-d-sulfoxide (BDS) reductase activity that is present in a strain lacking EG10124-MONOMER; torZ encodes a putative molybdoenzyme . Overexpression of torYZ allows anaerobic TMAO respiration in a strain (torC2::ΩSpcrΔdms Kmr) that otherwise grows extremely slowly with TMAO as terminal oxidant . TMAO and 4-methylmorpholine are good substrates in vitro; BSO, tetramethylene sulfoxide and DL-methionine sulfoxide are reduced less efficiently and DMSO acts as a competitive inhibitor . TorZ is exported to the periplasm via the Tat pathway . TorZ has 62% identity with the cytoplasmic EG10124-MONOMER "BSO reductase" and 42% identity with TORA-MONOMER "TorA" . torYZ expression is very low and is not induced by TMAO or DMSO .

## Biological Role

Catalyzes RXN-19619 (reaction.ecocyc.RXN-19619). Bound by a W/Mo-molybdopterin cofactor (molecule.ecocyc.Mo-molybdopterin-cofactor).

## Enriched Pathways

- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Reduces trimethylamine-N-oxide (TMAO) into trimethylamine; an anaerobic reaction coupled to energy-yielding reactions. Can also reduce other N- and S-oxide compounds such as 4-methylmorpholine-N-oxide and biotin sulfoxide (BSO), but with a lower catalytic efficiency. {ECO:0000269|PubMed:11004177}.

## Pathways

- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-19619|reaction.ecocyc.RXN-19619]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.Mo-molybdopterin-cofactor|molecule.ecocyc.Mo-molybdopterin-cofactor]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b1872|gene.b1872]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P46923`
- `KEGG:ecj:JW1861;eco:b1872;ecoc:C3026_10655;`
- `GeneID:946389;`
- `GO:GO:0009055; GO:0009061; GO:0030288; GO:0043546; GO:0046872; GO:0050626`
- `EC:1.7.2.3`

## Notes

Trimethylamine-N-oxide reductase 2 (TMAO reductase 2) (Trimethylamine oxidase 2) (EC 1.7.2.3)
