---
entity_id: "molecule.C00019"
entity_type: "small_molecule"
name: "S-Adenosyl-L-methionine"
source_database: "KEGG"
source_id: "C00019"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "S-Adenosyl-L-methionine"
  - "S-Adenosylmethionine"
  - "AdoMet"
  - "SAM"
---

# S-Adenosyl-L-methionine

`molecule.C00019`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00019`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: S-Adenosyl-L-methionine; S-Adenosylmethionine; AdoMet; SAM S-ADENOSYLMETHIONINE (AdoMet, SAM) is a sulfonium compound in which each of the carbons attached to the sulfur is activated toward nucleophilic attack. It is the most common methyl group donor for methyltransferase enzymes. In addition, AdoMet is cleaved reductively by a large number of iron-sulfur cluster-containing enzymes (known as radical SAM or radical AdoMet enzymes) to produce CPD-15400, which they use to activate their substrates. Another major role of AdoMet is in polyamine biosynthesis, where it is decarboxylated by EC-4.1.1.50, to form S-ADENOSYLMETHIONINAMINE, which serves as a propylamine group donor. AdoMet is formed by EC-2.5.1.6 and bears an S configuration at the sulfur atom. The chiral sulfonium of AdoMet spontaneously racemizes under physiological conditions to form a mixture of S and R isomers. This results in reduced activity, as the CPD0-2554 "R isomer" is not accepted as a substrate for AdoMet-dependent methyltransferases .

## Biological Role

Consumed as substrate in 108 reaction(s). Produced in 1 reaction(s). Binds epmB (protein.P39280).

## Enriched Pathways

- `eco00261` Monobactam biosynthesis (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco00999` Biosynthesis of various plant secondary metabolites (KEGG)
- `eco04122` Sulfur relay system (KEGG)
- `eco04981` Folate transport and metabolism (KEGG)

## Annotation

KEGG compound: S-Adenosyl-L-methionine; S-Adenosylmethionine; AdoMet; SAM

## Pathways

- `eco00261` Monobactam biosynthesis (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco00999` Biosynthesis of various plant secondary metabolites (KEGG)
- `eco04122` Sulfur relay system (KEGG)
- `eco04981` Folate transport and metabolism (KEGG)

## Outgoing Edges (114)

- `binds` --> [[protein.P39280|protein.P39280]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` --> [[complex.ecocyc.CPLX0-11744|complex.ecocyc.CPLX0-11744]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.MONOMER0-157|complex.ecocyc.MONOMER0-157]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.ecocyc.S-ADENMETSYN-RXN|reaction.ecocyc.S-ADENMETSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00177|reaction.R00177]] `KEGG` `database` - C00009 + C00013 + C00019 <=> C00002 + C00073 + C00001
- `is_substrate_of` --> [[reaction.R00178|reaction.R00178]] `KEGG` `database` - C00019 + C00080 <=> C01137 + C00011
- `is_substrate_of` --> [[reaction.R00380|reaction.R00380]] `KEGG` `database` - C00019 + C00039 <=> C00021 + C02967
- `is_substrate_of` --> [[reaction.R00594|reaction.R00594]] `KEGG` `database` - C00019 + C01764 <=> C00021 + C03446
- `is_substrate_of` --> [[reaction.R00597|reaction.R00597]] `KEGG` `database` - C00019 + C01977 <=> C00021 + C04157
- `is_substrate_of` --> [[reaction.R00600|reaction.R00600]] `KEGG` `database` - C00019 + C01977 <=> C00021 + C04160
- `is_substrate_of` --> [[reaction.R00601|reaction.R00601]] `KEGG` `database` - C00019 + C11478 <=> C00021 + C04728
- `is_substrate_of` --> [[reaction.R00650|reaction.R00650]] `KEGG` `database` - C00019 + C00155 <=> C00021 + C00073
- `is_substrate_of` --> [[reaction.R02623|reaction.R02623]] `KEGG` `database` - C00019 + C00614 <=> C00021 + C04142
- `is_substrate_of` --> [[reaction.R02917|reaction.R02917]] `KEGG` `database` - C00019 + C01977 <=> C00021 + C04545
- `is_substrate_of` --> [[reaction.R03194|reaction.R03194]] `KEGG` `database` - 2 C00019 + C01051 <=> 2 C00021 + C02463
- `is_substrate_of` --> [[reaction.R03411|reaction.R03411]] `KEGG` `database` - C00019 + C01229 <=> C00021 + C04340
- `is_substrate_of` --> [[reaction.R04710|reaction.R04710]] `KEGG` `database` - C00019 + C05196 + C05197 <=> C05198 + C00073 + C05199 + C05312
- `is_substrate_of` --> [[reaction.R05763|reaction.R05763]] `KEGG` `database` - C00019 + C02341 <=> C00021 + C11514
- `is_substrate_of` --> [[reaction.R06895|reaction.R06895]] `KEGG` `database` - C03263 + 2 C00019 <=> C01079 + 2 C00011 + 2 C00073 + 2 C05198
- `is_substrate_of` --> [[reaction.R07767|reaction.R07767]] `KEGG` `database` - C16236 + C22154 + 2 C00019 + 2 C22150 + 8 C00080 <=> C16832 + C22155 + 2 C00283 + 4 C14818 + 2 C00073 + 2 C05198 + 2 C22151
- `is_substrate_of` --> [[reaction.R10220|reaction.R10220]] `KEGG` `database` - C00019 + C20446 <=> C00073 + C00147 + C19647
- `is_substrate_of` --> [[reaction.R10246|reaction.R10246]] `KEGG` `database` - C00082 + C00019 + C00030 <=> C15809 + C01468 + C05198 + C00073 + C00028
- `is_substrate_of` --> [[reaction.ecocyc.1.97.1.4-A-RXN|reaction.ecocyc.1.97.1.4-A-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.2-OCTAPRENYL-6-OHPHENOL-METHY-RXN|reaction.ecocyc.2-OCTAPRENYL-6-OHPHENOL-METHY-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.2-OCTAPRENYL-METHOXY-BENZOQ-METH-RXN|reaction.ecocyc.2-OCTAPRENYL-METHOXY-BENZOQ-METH-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.2.1.1.34-RXN|reaction.ecocyc.2.1.1.34-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.2.1.1.72-RXN|reaction.ecocyc.2.1.1.72-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.2.1.1.77-RXN|reaction.ecocyc.2.1.1.77-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.2.1.1.79-RXN|reaction.ecocyc.2.1.1.79-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.2.5.1.25-RXN|reaction.ecocyc.2.5.1.25-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ADOMET-DMK-METHYLTRANSFER-RXN|reaction.ecocyc.ADOMET-DMK-METHYLTRANSFER-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.CHER-RXN|reaction.ecocyc.CHER-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.CHERTAPM-RXN|reaction.ecocyc.CHERTAPM-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.CHERTARM-RXN|reaction.ecocyc.CHERTARM-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.CHERTRGM-RXN|reaction.ecocyc.CHERTRGM-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.CHERTSRM-RXN|reaction.ecocyc.CHERTSRM-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.DAPASYN-RXN|reaction.ecocyc.DAPASYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.DHHB-METHYLTRANSFER-RXN|reaction.ecocyc.DHHB-METHYLTRANSFER-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.DNA-CYTOSINE-5--METHYLTRANSFERASE-RXN|reaction.ecocyc.DNA-CYTOSINE-5--METHYLTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.HEMN-RXN|reaction.ecocyc.HEMN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.HOMOCYSTEINE-S-METHYLTRANSFERASE-RXN|reaction.ecocyc.HOMOCYSTEINE-S-METHYLTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PYRIMSYN1-RXN|reaction.ecocyc.PYRIMSYN1-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RNTRACTIV-RXN|reaction.ecocyc.RNTRACTIV-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-11319|reaction.ecocyc.RXN-11319]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-11475|reaction.ecocyc.RXN-11475]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-11573|reaction.ecocyc.RXN-11573]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-11574|reaction.ecocyc.RXN-11574]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-11576|reaction.ecocyc.RXN-11576]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-11578|reaction.ecocyc.RXN-11578]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-11586|reaction.ecocyc.RXN-11586]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-11588|reaction.ecocyc.RXN-11588]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-11589|reaction.ecocyc.RXN-11589]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-11591|reaction.ecocyc.RXN-11591]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-11592|reaction.ecocyc.RXN-11592]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-11593|reaction.ecocyc.RXN-11593]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-11596|reaction.ecocyc.RXN-11596]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-11598|reaction.ecocyc.RXN-11598]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-11600|reaction.ecocyc.RXN-11600]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-11601|reaction.ecocyc.RXN-11601]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-11602|reaction.ecocyc.RXN-11602]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-11633|reaction.ecocyc.RXN-11633]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-11635|reaction.ecocyc.RXN-11635]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-11637|reaction.ecocyc.RXN-11637]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-11638|reaction.ecocyc.RXN-11638]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-11845|reaction.ecocyc.RXN-11845]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-11860|reaction.ecocyc.RXN-11860]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-11865|reaction.ecocyc.RXN-11865]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-11866|reaction.ecocyc.RXN-11866]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-11867|reaction.ecocyc.RXN-11867]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-12458|reaction.ecocyc.RXN-12458]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-12480|reaction.ecocyc.RXN-12480]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-13403|reaction.ecocyc.RXN-13403]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-14992|reaction.ecocyc.RXN-14992]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17473|reaction.ecocyc.RXN-17473]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17956|reaction.ecocyc.RXN-17956]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-19922|reaction.ecocyc.RXN-19922]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-20459|reaction.ecocyc.RXN-20459]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-21179|reaction.ecocyc.RXN-21179]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-25170|reaction.ecocyc.RXN-25170]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-25310|reaction.ecocyc.RXN-25310]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-7605|reaction.ecocyc.RXN-7605]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-8340|reaction.ecocyc.RXN-8340]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-8675|reaction.ecocyc.RXN-8675]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-1241|reaction.ecocyc.RXN0-1241]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-1342|reaction.ecocyc.RXN0-1342]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-2441|reaction.ecocyc.RXN0-2441]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-281|reaction.ecocyc.RXN0-281]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5063|reaction.ecocyc.RXN0-5063]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5144|reaction.ecocyc.RXN0-5144]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5194|reaction.ecocyc.RXN0-5194]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5419|reaction.ecocyc.RXN0-5419]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5437|reaction.ecocyc.RXN0-5437]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6366|reaction.ecocyc.RXN0-6366]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6515|reaction.ecocyc.RXN0-6515]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6576|reaction.ecocyc.RXN0-6576]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6731|reaction.ecocyc.RXN0-6731]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6734|reaction.ecocyc.RXN0-6734]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6950|reaction.ecocyc.RXN0-6950]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6998|reaction.ecocyc.RXN0-6998]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7007|reaction.ecocyc.RXN0-7007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7066|reaction.ecocyc.RXN0-7066]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7114|reaction.ecocyc.RXN0-7114]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7167|reaction.ecocyc.RXN0-7167]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7168|reaction.ecocyc.RXN0-7168]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7413|reaction.ecocyc.RXN0-7413]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7456|reaction.ecocyc.RXN0-7456]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-949|reaction.ecocyc.RXN0-949]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.SAMDECARB-RXN|reaction.ecocyc.SAMDECARB-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TDCEACT1-RXN|reaction.ecocyc.TDCEACT1-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRNA-GUANINE-N7--METHYLTRANSFERASE-RXN|reaction.ecocyc.TRNA-GUANINE-N7--METHYLTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRNA-URACIL-5--METHYLTRANSFERASE-RXN|reaction.ecocyc.TRNA-URACIL-5--METHYLTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.UROPORIIIMETHYLTRANSA-RXN|reaction.ecocyc.UROPORIIIMETHYLTRANSA-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.HOMSUCTRAN-RXN|reaction.ecocyc.HOMSUCTRAN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.S-ADENMETSYN-RXN|reaction.ecocyc.S-ADENMETSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00019`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
