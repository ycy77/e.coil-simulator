---
entity_id: "protein.Q46856"
entity_type: "protein"
name: "yqhD"
source_database: "UniProt"
source_id: "Q46856"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yqhD b3011 JW2978"
---

# yqhD

`protein.Q46856`

## Static

- Type: `protein`
- Source: `UniProt:Q46856`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Exhibits NADPH-dependent reductase activity for a broad range of short-chain aldehydes (PubMed:18211903, PubMed:19429550, PubMed:19609521, PubMed:20543070). Shows highest catalytic efficiency toward butanal, propanal and the highly toxic aldehydes acrolein and malondialdehyde (MDA), which are produced mainly during lipid peroxidation (PubMed:18211903, PubMed:20543070). Mediates resistance to reactive oxygen species (ROS) elicitors, such as paraquat and potassium tellurite, probably by protecting the cell against the toxic effects of reactive aldehydes derived from membrane lipid peroxidation (PubMed:18211903). Also acts, with lower efficiency, on acetaldehyde, glyceraldehyde, glycolaldehyde, methylglyoxal, glyoxal and hydroxyacetone (PubMed:18211903, PubMed:19609521, PubMed:20543070). Could be involved in glyoxal metabolism, by catalyzing the reduction of glyoxal to glycolaldehyde, and further to 1,2-ethandiol (PubMed:20543070). Catalyzes the reduction of isobutyraldehyde (2-methylpropanal) to isobutanol, and probably contributes to the production of isobutanol (PubMed:19609521). Can probably catalyze the reduction of glutaraldehyde, a widely used biocide, to 1,5-pentanediol, which is non-toxic (PubMed:34248896). Overexpression of YqhD protects the cells against glutaraldehyde toxicity (PubMed:34248896)...

## Biological Role

Component of NADPH-dependent aldehyde reductase YqhD (complex.ecocyc.CPLX0-7667).

## Enriched Pathways

- `eco00640` Propanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Exhibits NADPH-dependent reductase activity for a broad range of short-chain aldehydes (PubMed:18211903, PubMed:19429550, PubMed:19609521, PubMed:20543070). Shows highest catalytic efficiency toward butanal, propanal and the highly toxic aldehydes acrolein and malondialdehyde (MDA), which are produced mainly during lipid peroxidation (PubMed:18211903, PubMed:20543070). Mediates resistance to reactive oxygen species (ROS) elicitors, such as paraquat and potassium tellurite, probably by protecting the cell against the toxic effects of reactive aldehydes derived from membrane lipid peroxidation (PubMed:18211903). Also acts, with lower efficiency, on acetaldehyde, glyceraldehyde, glycolaldehyde, methylglyoxal, glyoxal and hydroxyacetone (PubMed:18211903, PubMed:19609521, PubMed:20543070). Could be involved in glyoxal metabolism, by catalyzing the reduction of glyoxal to glycolaldehyde, and further to 1,2-ethandiol (PubMed:20543070). Catalyzes the reduction of isobutyraldehyde (2-methylpropanal) to isobutanol, and probably contributes to the production of isobutanol (PubMed:19609521). Can probably catalyze the reduction of glutaraldehyde, a widely used biocide, to 1,5-pentanediol, which is non-toxic (PubMed:34248896). Overexpression of YqhD protects the cells against glutaraldehyde toxicity (PubMed:34248896). Can catalyze in vitro the NADPH-dependent reduction of furfural, a natural product of lignocellulosic decomposition, to the less toxic product, furfuryl alcohol (PubMed:19429550). However, it is unlikely that furfural is a physiological substrate (PubMed:19429550). {ECO:0000269|PubMed:18211903, ECO:0000269|PubMed:19429550, ECO:0000269|PubMed:19609521, ECO:0000269|PubMed:20543070, ECO:0000269|PubMed:34248896}.; FUNCTION: In contrast, Sulzenbacher et al. detected significant activities only in the presence of alcohol and NADP(+) (PubMed:15327949). They reported in vitro NADP(+)-dependent alcohol dehydrogenase (ADH) activity towards various alcohols, with a preference for alcohols longer than C(3), but the affinity for the substrates is poor, suggesting that these compounds are not the physiological substrates (PubMed:15327949). Perez et al. did not detect dehydrogenase activity with short and medium chain alcohols such as methanol, ethanol, propanol, butanol or isopropanol (PubMed:18211903). {ECO:0000269|PubMed:15327949, ECO:0000269|PubMed:18211903}.

## Pathways

- `eco00640` Propanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7667|complex.ecocyc.CPLX0-7667]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3011|gene.b3011]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q46856`
- `KEGG:ecj:JW2978;eco:b3011;ecoc:C3026_16460;`
- `GeneID:75173141;75203591;947493;`
- `GO:GO:0000302; GO:0005829; GO:0008106; GO:0008270; GO:0018455; GO:0042802; GO:0047655; GO:1990002; GO:1990362`
- `EC:1.1.1.2`

## Notes

NADPH-dependent aldehyde reductase YqhD (EC 1.1.1.2) (Alcohol dehydrogenase YqhD) (Alcohol/aldehyde oxidoreductase YqhD) (Broad-range ADH)
