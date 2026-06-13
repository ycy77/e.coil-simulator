---
entity_id: "protein.P0AEY3"
entity_type: "protein"
name: "mazG"
source_database: "UniProt"
source_id: "P0AEY3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mazG b2781 JW2752"
---

# mazG

`protein.P0AEY3`

## Static

- Type: `protein`
- Source: `UniProt:P0AEY3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the regulation of bacterial cell survival under conditions of nutritional stress. Regulates the type II MazE-MazF toxin-antitoxin (TA) system which mediates programmed cell death (PCD). This is achieved by lowering the cellular concentration of (p)ppGpp produced by RelA under amino acid starvation, thus protecting the cell from the toxicity of MazF. Reduction of (p)ppGpp can be achieved by direct degradation of (p)ppGpp or by degradation of NTPs, which are substrates for (p)ppGpp synthesis by RelA. {ECO:0000269|PubMed:16390452, ECO:0000269|PubMed:18353782, ECO:0000269|PubMed:20529853}. MazG is a nucleoside pyrophosphohydrolase that limits the deleterious effect of the MazF toxin under nutritional stress conditions . MazF belongs to the superfamily of all-α NTP pyrophosphatases. Members of this family are predicted to perform "house-cleaning" functions by hydrolyzing non-canonical NTPs . MazG exhibits pyrophosphohydrolase activity toward all four dNTPs and also exhibits (somewhat less) activity toward all four rNTPs . Hydrolysis of GTP is more efficient that hydrolysis of ATP . Addition of purified MazEF proteins causes inhibition of MazG enzymatic activity . MazG and Era associate in vitro and by yeast two-hybrid test. Nucleotide influences the association; binding is weaker with GTPγS than with GDP added...

## Biological Role

Catalyzes ATP diphosphohydrolase (diphosphate-forming); (reaction.R00087), NAD+ phosphohydrolase (reaction.R00103), FAD nucleotidohydrolase (reaction.R00160), UDP-glucose glucophosphohydrolase (reaction.R00287), GTP diphosphohydrolase (diphosphate-forming); (reaction.R00426), CTP diphosphohydrolase (diphosphate-forming); (reaction.R00515), uridine triphosphate pyrophosphohydrolase (reaction.R00662), nucleoside-triphosphate diphosphohydrolase (reaction.R01532). Component of nucleoside triphosphate pyrophosphohydrolase (complex.ecocyc.CPLX0-7692).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: Involved in the regulation of bacterial cell survival under conditions of nutritional stress. Regulates the type II MazE-MazF toxin-antitoxin (TA) system which mediates programmed cell death (PCD). This is achieved by lowering the cellular concentration of (p)ppGpp produced by RelA under amino acid starvation, thus protecting the cell from the toxicity of MazF. Reduction of (p)ppGpp can be achieved by direct degradation of (p)ppGpp or by degradation of NTPs, which are substrates for (p)ppGpp synthesis by RelA. {ECO:0000269|PubMed:16390452, ECO:0000269|PubMed:18353782, ECO:0000269|PubMed:20529853}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (9)

- `catalyzes` --> [[reaction.R00087|reaction.R00087]] `KEGG` `database` - via EC:3.6.1.9
- `catalyzes` --> [[reaction.R00103|reaction.R00103]] `KEGG` `database` - via EC:3.6.1.9
- `catalyzes` --> [[reaction.R00160|reaction.R00160]] `KEGG` `database` - via EC:3.6.1.9
- `catalyzes` --> [[reaction.R00287|reaction.R00287]] `KEGG` `database` - via EC:3.6.1.9
- `catalyzes` --> [[reaction.R00426|reaction.R00426]] `KEGG` `database` - via EC:3.6.1.9
- `catalyzes` --> [[reaction.R00515|reaction.R00515]] `KEGG` `database` - via EC:3.6.1.9
- `catalyzes` --> [[reaction.R00662|reaction.R00662]] `KEGG` `database` - via EC:3.6.1.9
- `catalyzes` --> [[reaction.R01532|reaction.R01532]] `KEGG` `database` - via EC:3.6.1.9
- `is_component_of` --> [[complex.ecocyc.CPLX0-7692|complex.ecocyc.CPLX0-7692]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2781|gene.b2781]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEY3`
- `KEGG:ecj:JW2752;eco:b2781;ecoc:C3026_15280;`
- `GeneID:93779217;947254;`
- `GO:GO:0005524; GO:0006203; GO:0009267; GO:0046047; GO:0046052; GO:0046061; GO:0046076; GO:0046081; GO:0046872; GO:0047429; GO:0047693`
- `EC:3.6.1.8`

## Notes

Nucleoside triphosphate pyrophosphohydrolase (NTP-PPase) (EC 3.6.1.8)
